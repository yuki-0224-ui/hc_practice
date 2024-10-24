from juice import Juice


class VendingMachine:
    def __init__(self):
        self.__juice_stock = [{"juice": Juice("ペプシ", 150), "stock": 5}]
        self.__sales_amount = 0

    @property
    def juice_stock(self):
        return [
            (item["juice"].name, item["juice"].price, item["stock"])
            for item in self.__juice_stock
        ]

    @property
    def sales_amount(self):
        return self.__sales_amount

    @property
    def available_juice(self):
        return [
            (item["juice"].name, item["juice"].price)
            for item in self.__juice_stock
            if item["stock"] > 0
        ]

    def add_juice(self, juice, stock):
        if stock <= 0:
            raise ValueError("在庫数は1以上を指定してください")

        for item in self.__juice_stock:
            if item["juice"].name == juice.name:
                item["stock"] += stock
                return

        self.__juice_stock.append({"juice": juice, "stock": stock})

    def buy_with_suica(self, juice_name, suica):
        stock_item = self.__find_stock(juice_name)
        if not stock_item:
            raise ValueError("そのジュースはありません")

        if stock_item["stock"] <= 0:
            raise ValueError("在庫切れです")

        try:
            suica.pay(stock_item["juice"].price)
            self.__reduce_stock(juice_name)
            self.__sales_amount += stock_item["juice"].price
        except ValueError as e:
            raise ValueError(e)

    def __find_stock(self, name):
        for item in self.__juice_stock:
            if item["juice"].name == name:
                return item
        return None

    def __reduce_stock(self, juice_name):
        stock_item = self.__find_stock(juice_name)
        if stock_item and stock_item["stock"] > 0:
            stock_item["stock"] -= 1
