from name_service import NameService


class Player(NameService):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
            return
        self.__name = new_name
