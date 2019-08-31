from peewee import SqliteDatabase
from peewee import Model
from setting import VK_DB_PATH

db = SqliteDatabase(VK_DB_PATH)

class BaseModel(Model):
    class Meta:
        database = db