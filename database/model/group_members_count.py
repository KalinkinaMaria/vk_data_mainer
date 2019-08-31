from peewee import IntegerField
from peewee import DateField
from peewee import ForeignKeyField

from database.model.base_model import BaseModel
from database.model.group import Group

class GroupMembersCount(BaseModel):
    count = IntegerField(default=0)
    date = DateField(unique=False)
    group_id = ForeignKeyField(Group)

GroupMembersCount.create_table()