"""
Module for insert, get, delete object Group from database
"""

from database.model.group_members_count import GroupMembersCount


def read():
    """
    Read all record from GroupMembersCount
    :return: list of GroupMembersCount
    """
    return GroupMembersCount.get()


def read_by_id(id):
    """
    Read record from GroupMembersCount by id
    :return: GroupMembersCount if exist else None
    """
    return GroupMembersCount.get(GroupMembersCount.id == id)


def persist(*args):
    """
    Save records GroupMembersCount
    """
    for item in args:
        if type(item) == GroupMembersCount:
            item.save()


def erase():
    """
    Clear all records GroupMembersCount
    """
    items = read()

    for item in items:
        item.delete_instance()