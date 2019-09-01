"""
Module for translator any object to Group
"""

from database.model.group import Group


def create_from_json_with_link(json_group, link):
    """
    Translator json to Group
    :param json_group: group as json
    :param link: link of group
    :return: group as Group
    """
    if json_group is None or link is None: 
        return None
    
    requeired_fields = ['id', 'screen_name']

    if not all([i in json_group and not json_group[i] is None for i in requeired_fields]): 
        return None

    group = Group()
    group.id = json_group['id']
    group.name = json_group['screen_name']
    group.link = link

    return group