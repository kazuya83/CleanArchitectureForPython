from AccountId import AccountId
from Activity import Activity
from Money import Money
from datetime import datetime

class ActivityWindow:
    """取引履歴
    """
    def __init__(self, activities: list[Activity]):
        self._activities = activities
    
    def __init__(self, *activities: Activity):
        self._activities: list[Activity] = list(activities)

    
    def getStartTimestamp(self) -> datetime:
        """取引履歴の最初のtimestamp
        """
        return min(self._activities, key=lambda e: e.timestamp)
    
    def getEndTimestamp(self) -> datetime:
        """取引履歴の最後のtimestamp
        """
        return max(self._activities, key=lambda e: e.timestamp)
    
    def calculateBalance(self, accountId: AccountId) -> Money:
        """取引履歴から残高を計算する
        """
        depositBalance = Money(sum(activity.amount for activity in self._activities if activity.targetAccountId == accountId))
        withdrawBalance = Money(sum(activity.amount for activity in self._activities if activity.sourceAccountId == accountId))
        return Money.Add(depositBalance, withdrawBalance.negate())

    def getActivities(self):
        return self._activities
    
    def addActivitiy(self, activity: Activity) -> None:
        self._activities.append(activity)
