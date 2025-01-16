from abc import ABC, abstractmethod
from db.connection import Connection


class AbstractMigration(ABC):
    def __init__(self, connection: Connection):
        self._db = connection

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass
