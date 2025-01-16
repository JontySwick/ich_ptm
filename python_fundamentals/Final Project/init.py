from pathlib import Path

import dotenv

from actions.back_action import BackAction
from actions.callback_action import CallbackAction
from actions.exit_action import ExitAction
from controllers.main_controller import MainController

dotenv.load_dotenv(Path('.env'))

actions: list = MainController().launch()
actions.append(ExitAction())
last_action = CallbackAction('Main', MainController().launch)
breadcrumbs = []

# Работаем пока пользователь сам не захочет выйти
while True:
    action = None
    # Не отпускаем пользователя пока он не выберет корректное действие
    while action is None:
        print('Select action:')

        for index, action in enumerate(actions, start=1):
            print(f'{index}. {action.get_title()}')

        try:
            user_action_index = int(input('Enter action number: '))

            if user_action_index > 0:
                action = actions[user_action_index - 1]
                actions = action.do_action()

                if type(action) is not BackAction:
                    breadcrumbs.append(last_action)

                if len(breadcrumbs):
                    actions.append(BackAction(breadcrumbs))

                if type(action) is not BackAction:
                    last_action = action
                else:
                    last_action = action.get_last_done_action()

                actions.append(ExitAction())
        except IndexError:
            pass
        except ValueError:
            pass
