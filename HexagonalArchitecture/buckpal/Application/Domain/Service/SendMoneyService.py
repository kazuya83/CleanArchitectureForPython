from Port.In.SendMoneyCommand import SendMoneyCommand
from Port.In.SendMoneyUseCase import SendMoneyUseCase
from Port.Out.LoadAccountPort import LoadAccountPort
from Port.Out.UpdateAccountStatePort import UpdateAccountStatePort
from MoneyTransferProperties import MoneyTransferProperties
from datetime import datetime, timedelta

class SendMoneyService(SendMoneyUseCase):
    def __init__(
            self,
            loadAccountPort: LoadAccountPort,
            updateAccountStatePort: UpdateAccountStatePort):
        self.loadAccountPort = loadAccountPort
        self.updateAccountStatePort = updateAccountStatePort

    def sendMoney(self, command: SendMoneyCommand) -> bool:
        self.checkThreshold(command)
        
        baselineDate: datetime = datetime.now - timedelta(days=10)
        
        sourceAccount = self.loadAccountPort.loadAccount(command.sourceAccountId, baselineDate)
        targetAccount = self.loadAccountPort.loadAccount(command.targetAccountId, baselineDate)

        if sourceAccount.getId().is_none():
            raise ValueError("expected source account ID not to be empty")
        if targetAccount.getId().is_none():
            raise ValueError("expected target account ID not to be empty")
        
        sourceAccountId = sourceAccount.getId().unwrap()
        targetAccountId = targetAccount.getId().unwrap()

        # TODO: account lockするべきか等のvalidation

        self.updateAccountStatePort.updateActivities(sourceAccount)
        self.updateAccountStatePort.updateActivities(targetAccount)

    def checkThreshold(self, command: SendMoneyCommand) -> None:
        if command.money.isGraterThan(MoneyTransferProperties.maximumTransferThreshold):
            raise ValueError("取引額上限を超えています")