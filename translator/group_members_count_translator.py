"""
Module for translator any object to GroupMembersCount
"""

from database.model.group_members_count import GroupMembersCount


def create_from_json_with_datetime(json_group, datetime):
    """
    Translator json to GroupMembersCount
    :param json_group: group as json
    :param datetime: datetime
    :return: group as GroupMembersCount
    """
    if json_group is None or datetime is None:
        return None
    
    requeired_fields = ['id', 'members_count']

    if not all([i in json_group and not json_group[i] is None for i in requeired_fields]):
        return None
    
    groupMembersCount = GroupMembersCount()
    groupMembersCount.count = json_group['members_count']
    groupMembersCount.date = datetime 
    groupMembersCount.group_id = json_group['id']

    return groupMembersCount