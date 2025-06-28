from Application.Domain.Model.AccountId import AccountId
from Application.Domain.Model.Money import Money

class SendMoneyCommand:
    def __init__(
            self,
            sourceAccountId: AccountId,
            targetAccountId: AccountId,
            money: Money):
        self._sourceAccountId = sourceAccountId
        self._targetAccountId = targetAccountId
        self._money = money

    @property
    def sourceAccountId(self) -> AccountId:
        return self._sourceAccountId
    
    @property
    def targetAccountId(self) -> AccountId:
        return self._targetAccountId
    
    @property
    def money(self) -> Money:
        return self._money
        