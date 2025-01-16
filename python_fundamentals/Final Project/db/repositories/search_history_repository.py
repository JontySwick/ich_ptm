import json

from db.repositories.abstract_repository import AbstractRepository


class SearchHistoryRepository(AbstractRepository):
    def _get_field_aliases(self) -> dict:
        return {}

    def get_by_search_type_and_params(self, search_type: str, **search_params):
        cursor = self._db.execute(
            '''
                SELECT id, search_params, search_type, count
                FROM search_history sh
                WHERE sh.search_type = %(search_type)s
                    AND sh.search_params = CAST(%(search_params)s AS JSON)
                LIMIT 1
            ''',
            {
                'search_type': search_type,
                'search_params': json.dumps(search_params)
            }
        )

        history_row = self._fetchone(cursor)
        cursor.close()

        return history_row


    def get_most_popular_search(self, search_type: str, limit: int = 10, offset: int = 0):
        cursor = self._db.execute(
            '''
                SELECT id, search_params, count
                FROM search_history sh
                WHERE sh.search_type = %(search_type)s
                ORDER BY count DESC
                LIMIT %(limit)s
            ''',
            {
                'search_type': search_type,
                'limit': limit,
                'offset': offset
            }
        )

        return self._fetchall(cursor)