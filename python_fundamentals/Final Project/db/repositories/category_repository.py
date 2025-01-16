from db.repositories.abstract_repository import AbstractRepository


class CategoryRepository(AbstractRepository):

    def _get_field_aliases(self) -> dict:
        return {}

    def get_all(self) -> list:
        cursor = self._db.execute(
            '''
                SELECT category_id, name 
                FROM category c 
            ''',
        )

        return self._fetchall(cursor)
