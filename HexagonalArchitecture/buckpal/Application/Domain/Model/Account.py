from Account import Account
from AccountId import AccountId
from Activity import Activity
from ActivityWindow import ActivityWindow
from datetime import datetime
from Money import Money
from option import Option

class Account:
    """
    一定額の管理を保有する口座
    * オブジェクトには、最新の口座取引履歴のウィンドウのみが含まれる。
    * 口座の合計残高は、ウィンドウ内の最初のアクティビティの前に有効だったベースライン残高とアクティビティ値の合計。
    """
    def __init__(self,
                 id: AccountId,
                 baselineBalance: Money,
                 activityWindow: ActivityWindow):
        """
        このクラスは直接インスタンス化しないでください。
        代わりに `Account.withoutId` or `Account.withId` を使ってください。
        """
        self._id = id
        self._baselineBalance = baselineBalance
        self._activityWindow = activityWindow

    @property
    def id(self) -> AccountId:
        return self._id
    
    @property
    def baselineBalance(self) -> Money:
        return self._baselineBalance
    
    @property
    def activityWindow(self) -> ActivityWindow:
        return self._activityWindow

    def withoutId(baselineBalance: Money, activityWindow: ActivityWindow) -> Account:
        """accountIdのないEntityの作成
        永続化されていない新しいEntityを作成時に使用
        """
        return Account(None, baselineBalance, activityWindow)
    
    def withId(id: AccountId, baselineBalance: Money, activityWindow: ActivityWindow) -> Account:
        """accountIdをもつEntityの作成
        永続化されたエンティティを再構築時に使用
        """
        return Account(id, baselineBalance, activityWindow)
    
    def getId(self) -> Option[AccountId]:
        return Option(AccountId) if self.id is None else Option.empty()
    
    def calculateBalance(self) -> Money:
        """取引履歴から合計残高を計算
        """
        return Money.add(self.baselineBalance, self.activityWindow.calculateBalance(self.id))
    
    def withdraw(self, money: Money, targetAccountId: AccountId) -> bool:
        """口座から一定額引き出す
        成功した場合、負の値を持つ新しいActivityを作成する。
        引き出しが成功した場合は true、失敗した場合は false を返却する。
        """
        if self.mayWithDraw(money) is not False:
            return False
        
        withdrawal = Activity(
            self.id,
            self.id,
            targetAccountId,
            datetime.now,
            money
        )
        self.activityWindow.addActivitiy(withdrawal)
        return True


    def mayWithDraw(self, money: Money) -> bool:
        return Money.add(self.calculateBalance(), money.negate()).isPositiveOrZero()