from Persistence.Entity.AccountEntity import AccountEntity

class AccountRepository:
    def __init__(self):
        # TODO: connectionとか渡されてくる？
        pass

    def findById(self, id: int) -> AccountEntity:
        # TODO: 本来はSQL等でDBからデータ取ってくる
        return AccountEntity(1)