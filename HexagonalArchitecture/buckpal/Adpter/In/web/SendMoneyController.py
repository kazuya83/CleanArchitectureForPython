from Application.Port.In.SendMoneyCommand import SendMoneyCommand
from Application.Domain.Model.AccountId import AccountId
from Application.Domain.Model.Money import Money
from Application.Domain.Service.SendMoneyService import SendMoneyService
from Application.Port.Out.LoadAccountPort import LoadAccountPort
from Common.AccountPersistenceAdpterBuilder import AccountPersistenceAdpterBuilder

class SendMoneyController:
    def sendMoney(sourceAccountId: int, targetAccountId: int, amount: int):
        """送金エンドポイント
        TODO: Flask等入れてpostMappingする
        """
        command = SendMoneyCommand(
            AccountId(sourceAccountId),
            AccountId(targetAccountId),
            Money(amount)
        )
        
        # TODO: DIする方が良い
        # TODO: AdpterはPortのInterfaceごとに分けても良いかも
        accountPersistenceAdpter = AccountPersistenceAdpterBuilder.build()
        SendMoneyService(accountPersistenceAdpter, accountPersistenceAdpter).sendMoney(command)
