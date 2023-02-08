import sqlite3
from pymongo import MongoClient


def connect_to_sqldb():
    conn = sqlite3.connect('semos_companies_data.db')
    return conn


def connect_to_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["semos_companies_data"]
    return db







