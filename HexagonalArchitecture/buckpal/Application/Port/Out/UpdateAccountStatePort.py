from abc import ABCMeta, abstractmethod
from Domain.Model.Account import Account

class UpdateAccountStatePort(ABCMeta):
    @abstractmethod
    def updateActivities(account: Account) -> None:
        raise NotImplementedError()