from actions.base_action import BaseAction


class CallbackAction(BaseAction):
    def __init__(self, title: str, callback: callable, *args, **kwargs):
        super().__init__(title)
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        self._callback = callback
        self._args = args
        self._kwargs = kwargs

    def do_action(self):
        return self._callback(*self._args, **self._kwargs)
