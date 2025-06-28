from AccountId import AccountId
from ActivityId import ActivityId
from datetime import datetime
from Money import Money

class Activity:
    """アカウント間の取引
    """
    
    def __init__(self,
                 activityId: ActivityId,
                 ownerAccountId: AccountId,
                 souceAccountId: AccountId,
                 targetAccountId: AccountId,
                 timestamp: datetime,
                 money: Money):
        self._activityId = activityId
        self._ownerAccountId = ownerAccountId
        self._sourceAccountId = souceAccountId
        self._targetAccountId = targetAccountId
        self._timestamp = timestamp
        self._money = money

    @property
    def activityId(self) -> ActivityId:
        return self._activityId
    
    @property
    def ownerAccountId(self) -> AccountId:
        return self._ownerAccountId
    
    @property
    def sourceAccountId(self) -> AccountId:
        return self._sourceAccountId
    
    @property
    def targetAccountId(self) -> AccountId:
        return self._targetAccountId
    
    @property
    def timestamp(self) -> AccountId:
        return self._timestamp
    
    @property
    def money(self) -> Money:
        return self._money
        