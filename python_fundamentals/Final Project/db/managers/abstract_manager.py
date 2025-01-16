from abc import ABC, abstractmethod

from db.connection import Connection


class AbstractManager(ABC):
    def __init__(self, connection: Connection):
        self._db = connection

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def delete(self, row_id: int):
        pass
