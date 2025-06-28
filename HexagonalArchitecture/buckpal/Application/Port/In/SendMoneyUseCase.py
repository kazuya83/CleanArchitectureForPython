from abc import ABCMeta, abstractmethod
from SendMoneyCommand import SendMoneyCommand

class SendMoneyUseCase(ABCMeta):
    @abstractmethod
    def sendMoney(self, command: SendMoneyCommand) -> bool:
        raise NotImplemented()