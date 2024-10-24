class Suica:
    __MINIMUM_CHARGE_AMOUNT = 100
    __INITIAL_BALANCE = 500

    @property
    def balance(self):
        return self.__balance

    def __init__(self):
        self.__balance = self.__INITIAL_BALANCE

    def charge(self, amount):
        if amount < self.__MINIMUM_CHARGE_AMOUNT:
            raise ValueError(
                f"チャージ金額は{self.__MINIMUM_CHARGE_AMOUNT}円以上からです"
            )
        self.__balance += amount

    def pay(self, amount):
        if amount > self.__balance:
            raise ValueError("残高不足です")
        self.__balance -= amount
