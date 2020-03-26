import pymongo
from pymongo import MongoClient

class DB:
	def __init__(self):
		self.client = MongoClient('localhost', 27017)