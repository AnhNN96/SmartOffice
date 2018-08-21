import sqlite3
from flask import g

DATABASE = './database/DbSmartOffice.sqlite'

class DatabaseDriver:
	def __init__(self):
		self.db = self.get_db()

	def get_db(self):
		db = getattr(g, '_database', None)
		if db is None:
			db = g._database = sqlite3.connect(DATABASE)
		return db

	def query_db(self, query, args=(), one=False):
		cur = self.db.execute(query, args)
		rv = cur.fetchall()
		cur.close()
		return (rv[0] if rv else None) if one else rv