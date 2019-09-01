"""
Base module for database model
"""

import sys

from peewee import SqliteDatabase
from peewee import Model
from setting import VK_DB_PATH

if hasattr(sys, "_called_from_test"):
    db = SqliteDatabase(':memory:')
else:
    db = SqliteDatabase(VK_DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db