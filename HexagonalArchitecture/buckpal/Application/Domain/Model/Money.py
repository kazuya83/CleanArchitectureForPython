from Money import Money

class Money:
    def __init__(self, amount: int,):
        """
        :param amount: 金額
        """
        if amount is None:
            raise ValueError("amount is required.")
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def ZERO():
        return Money(0)
    
    def isPositiveOrZero(self) -> bool:
        """正の数 or 0
        """
        return self.amount >= 0
    
    def isNegative(self) -> bool:
        """負の数
        """
        return self.amount < 0
    
    def isPositive(self) -> bool:
        return self.amount > 0
    
    def isGraterThanOrEqualTo(self, money: Money) -> bool:
        return self.amount >= money.amount
    
    def isGraterThan(self, money: Money) -> bool:
        return self.amount > money.amount
    
    def of(value: int) -> Money:
        return Money(value)
    
    def add(a: Money, b: Money) -> Money:
        return Money(a.amount + b.amount)
    
    def minus(self, money: Money) -> Money:
        return Money(self.amount - money.amount)
    
    def plus(self, money: Money) -> Money:
        return Money(self.amount + money.amount)

    def subtract(a: Money, b: Money) -> Money:
        return Money(a.amount - b.amount)
    
    def negate(self) -> Money:
        return Money(self.amount*-1)

