from Entity.AccountEntity import AccountEntity
from Entity.ActivityEntity import ActivityEntity
from Application.Domain.Model.Account import Account
from Application.Domain.Model.AccountId import AccountId
from Application.Domain.Model.Activity import Activity
from Application.Domain.Model.ActivityId import ActivityId
from Application.Domain.Model.ActivityWindow import ActivityWindow
from Application.Domain.Model.Money import Money

class ConverterEntity:
    def ConvertToAccount(
            account: AccountEntity,
            activities: list[ActivityEntity],
            withdrawalBalance: int,
            depositBalance: int) -> Account:
        baselineBalance = Money.subtract(Money.of(depositBalance), Money.of(withdrawalBalance))
        return Account.withId(AccountId(account.id), baselineBalance, ConverterEntity.ConvertToActivityWindow(activities))
    
    def ConvertToActivityWindow(activityEntities: list[ActivityEntity]) -> ActivityWindow: 
        activities: list[Activity] = []

        for entity in activityEntities:
            activities.append(Activity(
                ActivityId(entity.id),
                AccountId(entity.ownerAccountId),
                AccountId(entity.sourceAccountId),
                AccountId(entity.targetAccountId),
                entity.timestamp,
                Money.of(entity.amount)
            ))
        return ActivityWindow(activities)
    
    def ConvertToAcitivityEntity(activity: Activity) -> ActivityEntity:
        return ActivityEntity(
            activity.activityId.value if activity.activityId is not None else None,
            activity.timestamp,
            activity.ownerAccountId,
            activity.sourceAccountId,
            activity.targetAccountId,
            activity.money.amount
        )