from abc import ABC, abstractmethod

from actions.base_action import BaseAction


class BackAction(BaseAction):
    def __init__(self, breadcrumbs: list[BaseAction]):
        super().__init__('Back to ' + breadcrumbs[-1].get_title())
        self.__breadcrumbs = breadcrumbs
        self.__last_done_action = None

    def do_action(self):
        self.__last_done_action = self.__breadcrumbs.pop()
        return self.__last_done_action.do_action()

    def get_last_done_action(self):
        return self.__last_done_action
    