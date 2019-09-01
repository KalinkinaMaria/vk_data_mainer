"""
Module for vork with vk api group
"""

from vk.exceptions import VkAPIError

from network.api_client.base_api_client import api
from network.api_client.base_api_client import setting


class Field(object):
    MEMBER_COUNT_FILED = 'members_count'


def get_group_data(group_id, additional=None):
    """
    Get info about group 
    :param group_id: id group
    :param additional: additional fields for request result
    :return: result api as json
    """
    try:
        return api.groups.getById(group_id=group_id, fields=additional, v=setting.VK_API_VERSION)[0]
    except VkAPIError as e:
        return {'error': e.message}
    except Exception as e:
        return {'error': 'something went wrong'}