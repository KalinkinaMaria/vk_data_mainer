from database.model.group import Group

def read():
    return Group.get()


def read_by_id(id):
    try:
        return Group.get(Group.id == id)
    except Exception:
        return None


def persist(*args):
    for item in args:
        if type(item) == Group:
                item.save()

def erase():
    items = read()

    for item in items:
        item.delete_instance()