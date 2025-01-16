from db.repositories.abstract_repository import AbstractRepository


class FilmRepository(AbstractRepository):
    def _get_field_aliases(self) -> dict:
        return {
            'film_id': '№',
            'title': 'Name',
            'release_year': 'Year',
            'description': 'Description',
            'special_features': 'Tags',
        }

    def get_by_keyword(self, keyword: str, limit: int = 10, offset: int = 0):
        keyword = f'%{keyword.lower()}%'

        cursor = self._db.execute(
            '''
                SELECT film_id, title, release_year, description, special_features
                FROM film f
                WHERE LOWER(title) LIKE %(keyword)s
                    OR LOWER(description) LIKE %(keyword)s
                    OR LOWER(special_features) LIKE %(keyword)s
                ORDER BY film_id
                LIMIT %(limit)s
                OFFSET %(offset)s
            ''',
            {
                'keyword': keyword,
                'limit': limit,
                'offset': offset
            }
        )

        return self._fetchall(cursor)

    def get_by_category_and_year(self, category_id: int, year: int, limit: int = 10, offset: int = 0):
        cursor = self._db.execute(
            '''
                SELECT f.film_id, f.title, f.release_year, f.description, f.special_features
                FROM film f
                INNER JOIN film_category fc ON fc.film_id = f.film_id
                    AND fc.category_id = %(category_id)s
                WHERE f.release_year = %(year)s
                    AND fc.category_id = %(category_id)s
                ORDER BY film_id
                LIMIT %(limit)s
                OFFSET %(offset)s
            ''',
            {
                'category_id': category_id,
                'year': year,
                'limit': limit,
                'offset': offset
            }
        )

        return self._fetchall(cursor)

    def get_years_range(self):
        cursor = self._db.execute(
            '''
                SELECT MIN(release_year) min, MAX(release_year) max
                FROM film f
            ''',
        )

        years_range = self._fetchone(cursor)
        cursor.close()

        return years_range