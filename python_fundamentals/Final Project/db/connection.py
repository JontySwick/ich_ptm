from abc import ABC, abstractmethod
from typing import Union

import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract
from mysql.connector.pooling import PooledMySQLConnection


class Connection(ABC):
    _instance = None

    def __init__(self):
        self._connection: Union[PooledMySQLConnection, MySQLConnectionAbstract, None] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self):
        if self._connection is None:
            self._connection = mysql.connector.connect(**self._get_db_config())

        return self._connection

    def close(self):
        if self._connection is not None:
            self._connection.close()

    def execute(self, query: str, params=()) -> MySQLCursorAbstract:
        cursor = self.connect().cursor()

        cursor.reset()
        cursor.execute(query, params)

        return cursor

    @abstractmethod
    def _get_db_config(self) -> dict:
        pass
