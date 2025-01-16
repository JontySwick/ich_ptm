from pathlib import Path

import dotenv

from db.migrations.abstract_migration import AbstractMigration
from db.write_connection import WriteConnection


class AddHistoryTable(AbstractMigration):
    def up(self):
        self._db.execute('''
            CREATE TABLE IF NOT EXISTS search_history (
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                search_params JSON NOT NULL,
                search_type ENUM('keyword', 'genre_and_year') NOT NULL,
                count INT NOT NULL DEFAULT 1
            );
        ''')

    def down(self):
        self._db.execute('''
            DROP TABLE search_history
        ''')
