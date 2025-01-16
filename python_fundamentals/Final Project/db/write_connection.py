import os
from db.connection import Connection


class WriteConnection(Connection):
    def _get_db_config(self) -> dict:
        return {
            'host': os.environ.get('DB_WRITE_HOST'),
            'user': os.environ.get('DB_WRITE_USER'),
            'password': os.environ.get('DB_WRITE_PASSWORD'),
            'database': '290724-ptm_fd_Kirill_Maiorov '
        }
