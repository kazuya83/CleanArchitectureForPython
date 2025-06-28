from Application.Port.Out.LoadAccountPort import LoadAccountPort
from Application.Port.Out.UpdateAccountStatePort import UpdateAccountStatePort
from Application.Domain.Model.Account import Account
from Application.Domain.Model.AccountId import AccountId
from Adpter.Out.Persistence.Repository.AccountRepository import AccountRepository
from Adpter.Out.Persistence.Repository.ActivityRepository import ActivityRepository
from ConverterEntity import ConverterEntity

class AccountPersistenceAdpter(LoadAccountPort, UpdateAccountStatePort):
    def __init__(
            self,
            accountRepository: AccountRepository,
            activityRepository: ActivityRepository):
        self.accountRepository = accountRepository
        self.activityRepository = activityRepository

    def loadAccount(self, accountId: AccountId, baselineDate):
        accountEntity = self.accountRepository.findById(accountId.value)
        if accountEntity is None:
            raise ValueError("Not Found account")
        
        activities = self.activityRepository.findByOwnerSince(accountId.value, baselineDate)
        withdrawalBalance = self.activityRepository.getWithdrawalBalanceUntil(accountId.value, baselineDate)
        depositBalance = self.activityRepository.getDepositBalanceUntil(accountId.value, baselineDate)

        return ConverterEntity.ConvertToAccount(accountEntity, activities, withdrawalBalance, depositBalance)
        
    def updateActivities(self, account: Account) -> None:
        for activity in account.activityWindow.getActivities():
            if activity.activityId is None:
                self.activityRepository.save(ConverterEntity.ConvertToAcitivityEntity(activity))

