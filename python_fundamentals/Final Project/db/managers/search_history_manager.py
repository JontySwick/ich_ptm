import json

from db.managers.abstract_manager import AbstractManager


class SearchHistoryManager(AbstractManager):
    def create(self, search_params, search_type, *kwargs):
        cursor = self._db.execute(
            '''
                INSERT INTO search_history
                SET search_params = %(search_params)s, 
                    search_type = %(search_type)s
            ''',
            {
                'search_params': json.dumps(search_params),
                'search_type': search_type
            }
        )
        self._db.connect().commit()

        return cursor.lastrowid

    def update(self, row_id, count, *kwargs):
        cursor = self._db.execute(
            '''
                UPDATE search_history
                SET count = %(count)s
                WHERE id = %(id)s
            ''',
            {
                'id': row_id,
                'count': count
            }
        )
        self._db.connect().commit()

        return cursor.lastrowid

    def delete(self, row_id: int):
        self._db.execute(
            '''
                DELETE FROM TABLE search_history
                WHERE id = %(id)s
            ''',
            {
                'id': row_id
            }
        )
        self._db.connect().commit()
