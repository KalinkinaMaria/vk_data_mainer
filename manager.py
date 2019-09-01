"""
Module for organization work with interaction VK API results
and writes it to database
"""

from datetime import datetime
from urllib.parse import urlparse

from network.api_client import group_api_client
from database.dao import group_dao
from database.dao import group_members_count_dao
from translator import group_translator as gt
from translator import group_members_count_translator as gmct


def get_group_name_from_link(link):
    """
    Parse link of VK group to group name
    :param link: link of group
    :return: name of group
    """
    scheme = ['https://', 'http://']
    parsered_link = urlparse(link if any([link.startswith(i) for i in scheme]) else scheme[0] + link)
    path = parsered_link.path

    if path.startswith('/'):
        path = path[1:]
    if path.endswith('/'):
        path = path[:len(path)-1]

    return path if not '/' in path else ''


def group_mining(group_link):
    """
    Maining data of members count of group
    :param group_link: link of group
    :raise: error with parse link and error from api
    """
    group_name = get_group_name_from_link(group_link)
    if len(group_name) == 0:
        raise Exception(f"faild with parse link of group: {group_link}")

    group_info = group_api_client.get_group_data(
        group_name, 
        additional=group_api_client.Field.MEMBER_COUNT_FILED
    )

    if 'error' in group_info:
        raise Exception(group_info['error'])
    
    db_group = gt.create_from_json_with_link(group_info, group_link)
    if group_dao.read_by_id(db_group.id) is None:
        group_dao.persist(db_group)
    
    db_group_member_count = gmct.create_from_json_with_datetime(group_info, datetime.now())
    group_members_count_dao.persist(db_group_member_count)
