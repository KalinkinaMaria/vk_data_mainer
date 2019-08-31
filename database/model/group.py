from peewee import CharField
from peewee import IntegerField
from peewee import DateField
from peewee import ForeignKeyField

from database.model.base_model import BaseModel

class Group(BaseModel):
    id = IntegerField(primary_key=True)
    link = CharField(unique=False)
    name = CharField(unique=False)

Group.create_table()