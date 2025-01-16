from abc import ABC, abstractmethod

from mysql.connector.abstracts import MySQLCursorAbstract

from db.connection import Connection


class AbstractRepository(ABC):
    def __init__(self, connection: Connection):
        self._db = connection

    def _get_column_names(self, cursor: MySQLCursorAbstract):
        column_aliases = self._get_field_aliases()

        return list(
            map(
                lambda column_props:
                column_aliases.get(column_props[0])
                if column_aliases.get(column_props[0])
                else column_props[0],
                cursor.description
            )
        )

    def _fetchone(self, cursor: MySQLCursorAbstract):
        if row := cursor.fetchone():
            return dict(zip(self._get_column_names(cursor), row))

        return {}

    def _fetchall(self, cursor: MySQLCursorAbstract):
        column_names = self._get_column_names(cursor)

        elements = []
        for row in cursor.fetchall():
            elements.append(dict(zip(column_names, row)))

        return elements

    @abstractmethod
    def _get_field_aliases(self) -> dict:
        pass
