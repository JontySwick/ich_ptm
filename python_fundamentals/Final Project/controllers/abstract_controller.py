from abc import ABC


class AbstractController(ABC):
    def _safe_input(self,
                    input_title: str = '',
                    input_callback: callable = None,
                    validation_func: callable = None,
                    error_message: str = ''
                    ):
        while True:
            try:
                user_input = input_callback(input(input_title))

                if not validation_func or validation_func(user_input):
                    return user_input
            except BaseException:
                if error_message:
                    print(error_message)


    def _show_list(self, list_to_show: ({})):
        for index, element in enumerate(list_to_show, 1):
            print('=' * 120)
            for prop_name, prop_value in element.items():
                if prop_name == 'id':
                    prop_name = '№'
                    prop_value = index

                if type(prop_value) in [dict, set, tuple, list]:
                    if type(prop_value) is dict:
                        prop_value = [f'\n\t{key.title()}: {value}' for key, value in prop_value.items()]

                    prop_value = ', '.join(prop_value)

                print(f'{prop_name}: {prop_value}')
        print('=' * 120)
