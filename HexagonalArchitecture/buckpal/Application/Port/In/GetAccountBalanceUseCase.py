from abc import ABCMeta, abstractmethod
from Domain.Model.Money import Money
from AccountBalanceQuery import GetAccountBalanceQuery

class GetAccountBalanceUseCase(ABCMeta):
    @abstractmethod
    def getAccountBalance(self, query: GetAccountBalanceQuery) -> Money:
        raise NotImplementedError()

