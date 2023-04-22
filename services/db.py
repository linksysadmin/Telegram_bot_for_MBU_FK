import os
from typing import Any
import sqlite3
import logging

from config import BASE_DIR

logger = logging.getLogger(__name__)


def execute(sql: str, params: tuple) -> None:
    con = sqlite3.connect(os.path.join(BASE_DIR, 'database.db'))
    cur = con.cursor()
    cur.execute(sql, params)
    con.commit()
    con.close()


def fetch_all(sql: str, params: Any | None = None) -> list[tuple]:
    con = sqlite3.connect(os.path.join(BASE_DIR, 'database.db'))
    cur = con.cursor()
    res = cur.execute(sql, params)
    rows = res.fetchall()
    con.close()
    return rows



if __name__ == '__main__':
    pass
