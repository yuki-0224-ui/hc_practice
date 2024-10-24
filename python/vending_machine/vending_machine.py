class VendingMachine:
    def __init__(self):
        self.__juice_stock = {"ペプシ": [150, 5]}
        self.__sales_amount = 0

    @property
    def juice_stock(self):
        return [(key, value[1]) for key, value in self.__juice_stock.items()]

    @property
    def sales_amount(self):
        return self.__sales_amount

    @property
    def available_juice(self):
        return [
            (key, value[0])
            for key, value in self.__juice_stock.items()
            if self.__juice_stock[key][1] > 0
        ]

    def add_juice(self, juice, stock):
        if stock <= 0:
            raise ValueError("在庫数は1以上を指定してください")
        if juice.name in self.__juice_stock:
            self.__juice_stock[juice.name][1] += stock
        else:
            self.__juice_stock[juice.name] = [juice.price, stock]

    def buy_with_suica(self, juice_name, suica):
        if juice_name not in self.__juice_stock:
            raise ValueError("そのジュースはありません")

        if not self.__has_stock(juice_name):
            raise ValueError("在庫切れです")

        price = self.__juice_stock[juice_name][0]

        try:
            suica.pay(price)
            self.__reduce_stock(juice_name)
            self.__sales_amount += price
        except ValueError as e:
            raise ValueError(e)

    def __has_stock(self, juice_name):
        return self.__juice_stock.get(juice_name, [0, 0])[1] > 0

    def __reduce_stock(self, juice_name):
        if self.__has_stock(juice_name):
            self.__juice_stock[juice_name][1] -= 1
