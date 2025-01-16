from abc import ABC, abstractmethod

from actions.base_action import BaseAction


class ExitAction(BaseAction):
    def __init__(self):
        super().__init__('Exit')

    def do_action(self):
        exit()


    