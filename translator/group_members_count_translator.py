from datetime import datetime

from database.model.group_members_count import GroupMembersCount

def create_from_json(json_group):
    if json_group is None:
        return None
    
    requeired_fields = ['id', 'members_count']

    if not all([i in json_group and not json_group[i] is None for i in requeired_fields]):
        return None
    
    groupMembersCount = GroupMembersCount()
    groupMembersCount.count = json_group['members_count']
    groupMembersCount.date = datetime.now()
    groupMembersCount.group_id = json_group['id']

    return groupMembersCount