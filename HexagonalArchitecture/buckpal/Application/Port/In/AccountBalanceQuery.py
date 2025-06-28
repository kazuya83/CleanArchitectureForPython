from Domain.Model.AccountId import AccountId
from CleanArchitectureForPython.HexagonalArchitecture.buckpal.Application.Port.In.AccountBalanceQuery import IGetAccountBalanceQuery

class GetAccountBalanceQuery:
    def __init__(self, accountId: AccountId):
        self._accountId = accountId

    @property
    def accountId(self) -> AccountId:
        return self._accountId