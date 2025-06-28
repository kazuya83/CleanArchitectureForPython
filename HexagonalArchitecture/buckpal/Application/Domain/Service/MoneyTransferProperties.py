from Domain.Model.Money import Money

class MoneyTransferProperties:
    @property
    def maximumTransferThreshold() -> Money:
        return Money(1000000)