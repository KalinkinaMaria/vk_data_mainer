"""
Module for insert, get, delete object Group from database
"""

from database.model.group import Group


def read():
    """
    Read all record from Group
    :return: list of Group
    """
    return Group.get()


def read_by_id(_id):
    """
    Read record from Group by id
    :return: Group if exist else None
    """
    try:
        return Group.get(Group.id == _id)
    except Exception:
        return None


def persist(*args):
    """
    Save records Group
    """
    for item in args:
        if type(item) == Group:
                item.save(force_insert=True)


def erase():
    """
    Clear all records Group
    """
    items = read()

    for item in items:
        item.delete_instance()