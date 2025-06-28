from datetime import datetime

class ActivityEntity:
    def __init__(
            self,
            id: int,
            timestamp: datetime,
            ownerAccountId: int,
            sourceAccountId: int,
            targetAccountId: int,
            amount: int):
        self._id = id
        self._timestamp = timestamp
        self._ownerAccountId = ownerAccountId
        self._sourceAccountId = sourceAccountId
        self._targetAccountId = targetAccountId
        self._amount = amount

    @property
    def id(self):
        return self._id
    
    @property
    def timestamp(self):
        return self._timestamp
    
    @property
    def ownerAccountId(self):
        return self._ownerAccountId
    
    @property
    def sourceAccountId(self):
        return self._sourceAccountId
    
    @property
    def targetAccountId(self):
        return self._targetAccountId
    
    @property
    def amount(self):
        return self._amount
