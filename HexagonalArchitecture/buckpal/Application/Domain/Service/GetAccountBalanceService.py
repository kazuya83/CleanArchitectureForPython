from Application.Port.In.GetAccountBalanceUseCase import GetAccountBalanceUseCase
from CleanArchitectureForPython.HexagonalArchitecture.buckpal.Application.Port.In.AccountBalanceQuery import GetAccountBalanceQuery
from Application.Port.Out.LoadAccountPort import LoadAccountPort
from datetime import datetime
from Application.Domain.Model.Money import Money

class GetAccountBalanceService(GetAccountBalanceUseCase):
    def __init__(self, loadAccountPort: LoadAccountPort):
        self.loadAccountPort = loadAccountPort
        
    def getAccountBalance(self, query: GetAccountBalanceQuery) -> Money:
        return self.loadAccountPort.loadAccount(query.accountId, datetime.now).calculateBalance()
