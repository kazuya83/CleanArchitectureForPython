from Entity.ActivityEntity import ActivityEntity
from datetime import datetime
from option import Option

class ActivityRepository:
    def __init__(self):
        # TODO: connectionとか渡されてくる？
        pass

    def findByOwnerSince(self, ownerAccountId: int, since: datetime) -> list[ActivityEntity]:
        # TODO: 本来はSQL等でDBからデータ取ってくる
        return []
    
    def getDepositBalanceUntil(self, accountId: int, until: datetime) -> Option[int]:
        # TODO: 本来はSQL等でDBからデータ取ってくる
        return Option(1)
    
    def getWithdrawalBalanceUntil(self, accountId: int, until: datetime) -> Option[int]:
        # TODO: 本来はSQL等でDBからデータ取ってくる
        return Option(1)
    
    def save(self, activity: ActivityEntity) -> None:
        # TODO: 本来はSQL等でDB更新に書き換えをする
        pass