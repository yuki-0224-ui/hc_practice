from abc import ABC, abstractmethod


class NameService(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, new_name):
        pass
