from database.model.group import Group

def read():
    return Group.get()


def read_by_id(_id):
    try:
        return Group.get(Group.id == _id)
    except Exception:
        return None


def persist(*args):
    for item in args:
        if type(item) == Group:
                item.save(force_insert=True)

def erase():
    items = read()

    for item in items:
        item.delete_instance()