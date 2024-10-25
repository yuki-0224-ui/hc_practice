from abc import abstractmethod
from name_service import NameService


class Pokemon(NameService):
    def __init__(self, name, type1, type2, hp):
        self.__name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
            return
        self.__name = new_name

    @abstractmethod
    def attack(self):
        pass
