import sqlite3


CONN = sqlite3.connect("league.db")
CURSOR = CONN.cursor()
