from database.model.group_members_count import GroupMembersCount


def read():
    return GroupMembersCount.get()


def read_by_id(id):
    return GroupMembersCount.get(GroupMembersCount.id == id)


def persist(*args):
    for item in args:
        if type(item) == GroupMembersCount:
            item.save()


def erase():
    items = read()

    for item in items:
        item.delete_instance()