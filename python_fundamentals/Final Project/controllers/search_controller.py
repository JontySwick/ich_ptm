from actions.callback_action import CallbackAction
from controllers.abstract_controller import AbstractController
from db.managers.search_history_manager import SearchHistoryManager
from db.read_connection import ReadConnection
from db.repositories.category_repository import CategoryRepository
from db.repositories.film_repository import FilmRepository
from db.repositories.search_history_repository import SearchHistoryRepository
from db.write_connection import WriteConnection


class SearchController(AbstractController):
    def __init__(self):
        self._film_repository = FilmRepository(ReadConnection())
        self._category_repository = CategoryRepository(ReadConnection())
        self._search_history_repository = SearchHistoryRepository(WriteConnection())
        self._search_history_manager = SearchHistoryManager(WriteConnection())

    def get_search_types_action(self):
        return [
            CallbackAction('Search by keywords', self.search_action, 'keyword'),
            CallbackAction('Search by genre and year', self.search_action, 'genre_and_year'),
        ]

    def search_action(self, search_type):
        actions = None
        if search_type == 'keyword':
            actions = self.search_by_keyword_action()
        elif search_type == 'genre_and_year':
            actions = self.search_by_genre_and_year()

        return actions

    def search_by_keyword_action(self) -> list:
        keyword = self._safe_input(
            'Enter keyword for search: ',
            lambda user_input: str.strip(user_input).lower(),
            lambda user_input: len(user_input) > 0
        )
        films = self._film_repository.get_by_keyword(keyword)

        self._show_list(films)
        self.__add_to_search_history('keyword', keyword=keyword)

        return []

    def search_by_genre_and_year(self) -> list:
        print('Select genre:')

        categories = self._category_repository.get_all()
        for index, category in enumerate(categories, 1):
            print(f'{index}. {category["name"]}')

        category_id = self._safe_input(
            'Enter gener number: ',
            lambda user_input_index: categories[int(user_input_index)]['category_id']
        )

        years_range = self._film_repository.get_years_range()
        year = self._safe_input(
            f'Enter year between {years_range["min"]} and {years_range["max"]}: ',
            int,
            lambda user_input_year: years_range['min'] <= user_input_year <= years_range['max']
        )

        films = self._film_repository.get_by_category_and_year(category_id, year)

        self._show_list(films)
        self.__add_to_search_history('genre_and_year', category_id=category_id, year=year)

        return []

    def __add_to_search_history(self, search_type, **search_params):
        if history_row := self._search_history_repository.get_by_search_type_and_params(search_type, **search_params):
            self._search_history_manager.update(history_row['id'], history_row['count'] + 1)
        else:
            self._search_history_manager.create(search_params, search_type)
