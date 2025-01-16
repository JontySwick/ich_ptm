from actions.callback_action import CallbackAction
from controllers.abstract_controller import AbstractController
from controllers.statistics_controller import StatisticsController
from controllers.search_controller import SearchController


class MainController(AbstractController):
    def launch(self):
        search_controller = SearchController()
        statistics_controller = StatisticsController()

        return [
            CallbackAction('Search', search_controller.get_search_types_action),
            CallbackAction('Show most popular requests', statistics_controller.get_statistics_types_action),
        ]
