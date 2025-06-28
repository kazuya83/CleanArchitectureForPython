class AccountEntity:
    def __init__(self, id: int):
        self._id = id

    @property
    def id(self):
        return self.id
