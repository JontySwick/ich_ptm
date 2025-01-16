import json

from actions.callback_action import CallbackAction
from controllers.abstract_controller import AbstractController
from db.read_connection import ReadConnection
from db.repositories.category_repository import CategoryRepository
from db.repositories.search_history_repository import SearchHistoryRepository
from db.write_connection import WriteConnection


class StatisticsController(AbstractController):
    def __init__(self):
        self._search_history_repository = SearchHistoryRepository(WriteConnection())
        self._category_repository = CategoryRepository(ReadConnection())

    def get_statistics_types_action(self):
        return [
            CallbackAction('Most popular by keywords', self.get_statistics_action, 'keyword'),
            CallbackAction('Most popular by genre and year', self.get_statistics_action, 'genre_and_year'),
        ]

    def get_statistics_action(self, search_type):
        if search_type in ['keyword', 'genre_and_year']:
            top_of_search = self._search_history_repository.get_most_popular_search(search_type)

            categories = {}
            if search_type == 'genre_and_year':
                categories = {category['category_id']: category for category in self._category_repository.get_all()}

            for row in top_of_search:
                search_params: dict = json.loads(row['search_params'])
                if search_type == 'genre_and_year':
                    category = categories.get(search_params['category_id'])
                    search_params['category'] = category['name'] if category else 'Removed category'
                    del search_params['category_id']

                row['Search condition'] = search_params
                del row['search_params']

            self._show_list(top_of_search)

        return []
