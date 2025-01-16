from abc import ABC, abstractmethod


class BaseAction(ABC):
    def __init__(self, title: str):
        self.__title = title

    def get_title(self):
        return self.__title

    @abstractmethod
    def do_action(self):
        pass
