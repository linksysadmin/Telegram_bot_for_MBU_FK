from typing import Any
import sqlite3
import logging

logger = logging.getLogger(__name__)


def execute(sql: str, params: list[tuple]) -> None:
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute(sql, params)


def fetch_all(sql: str, params: Any | None = None) -> list[tuple]:
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute(sql, params)
    rows = res.fetchall()
    results = []
    for row in rows:
        results.append(row)
    return results


if __name__ == '__main__':
    pass
