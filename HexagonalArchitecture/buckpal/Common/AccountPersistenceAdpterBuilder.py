from Adpter.Out.Persistence.AccountPersistenceAdpter import AccountPersistenceAdpter
from Adpter.Out.Persistence.Repository.AccountRepository import AccountRepository
from Adpter.Out.Persistence.Repository.ActivityRepository import ActivityRepository

class AccountPersistenceAdpterBuilder:
    def build() -> AccountPersistenceAdpter:
        return AccountPersistenceAdpter(AccountRepository(), ActivityRepository())