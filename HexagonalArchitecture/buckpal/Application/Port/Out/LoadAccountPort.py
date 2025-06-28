from abc import ABCMeta, abstractmethod
from Domain.Model.Account import Account
from Domain.Model.AccountId import AccountId
from datetime import datetime

class LoadAccountPort(ABCMeta):
    @abstractmethod
    def loadAccount(self, accountId: AccountId, baselineDate: datetime) -> Account:
        raise NotImplementedError()