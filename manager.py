from urllib.parse import urlparse

from network.api_client import group_api_client
from database.dao import group_dao
from database.dao import group_members_count_dao
from translator import group_translator as gt
from translator import group_members_count_translator as gmct


# test
def get_group_name_from_link(link):
    scheme = 'https://'
    parsered_link = urlparse(link if link.startswith(scheme) else scheme + link)
    return parsered_link.path.replace('/', '')


def group_mining(group_link):
    group_name = get_group_name_from_link(group_link)
    if len(group_name) == 0:
        return False

    group_info = group_api_client.get_group_data(
        group_name, 
        additional=group_api_client.Field.MEMBER_COUNT_FILED
    )

    if 'error' in group_info:
        print(group_info['error'])
        return False
    
    db_group = gt.create_from_json_with_link(group_info, group_link)
    if group_dao.read_by_id(db_group.id) is None:
        group_dao.persist(db_group)
    
    db_group_member_count = gmct.create_from_json(group_info)
    group_members_count_dao.persist(db_group_member_count)

    return True