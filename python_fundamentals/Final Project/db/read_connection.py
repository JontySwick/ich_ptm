import os
from db.connection import Connection


class ReadConnection(Connection):
    def _get_db_config(self) -> dict:
        return {
            'host': os.environ.get('DB_READ_HOST'),
            'user': os.environ.get('DB_READ_USER'),
            'password': os.environ.get('DB_READ_PASSWORD'),
            'database': 'sakila'
        }
