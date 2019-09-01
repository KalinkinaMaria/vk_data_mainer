import datetime

import pytest

from database.model.group_members_count import Group
from database.model.group_members_count import GroupMembersCount
from translator.group_members_count_translator import create_from_json_with_datetime


def setup_module(module):
    test_group = Group(id=111, name='test', link='vk.com/test')
    test_group.save(force_insert=True)


def test_correct():
    input_json = {
        'id': 111,
        'members_count': 111
    }
    input_date = datetime.datetime.now()
    group_member_count = GroupMembersCount(count=111, group_id=111, date=input_date)
    output_group_member_count = create_from_json_with_datetime(input_json, input_date)

    assert group_member_count.group_id == output_group_member_count.group_id and \
        group_member_count.count == output_group_member_count.count and \
        group_member_count.date == output_group_member_count.date



def test_json_is_none():
    input_json = None
    input_date = datetime.datetime.now()
    out_group_members_count = create_from_json_with_datetime(input_json, input_date)
    
    assert out_group_members_count is None


def test_datetime_is_none():
    input_json = {
        'id': 111,
        'members_count': 111
    }
    input_date = None
    out_group_members_count = create_from_json_with_datetime(input_json, input_date)
    
    assert out_group_members_count is None


def test_json_is_none_and_link_is_none():
    input_json = None
    input_date = None
    out_group_members_count = create_from_json_with_datetime(input_json, input_date)
    
    assert out_group_members_count is None


def test_dont_containse_id():
    input_json = {
        'members_count': 111
    }
    input_date = datetime.datetime.now()
    out_group_members_count = create_from_json_with_datetime(input_json, input_date)
    
    assert out_group_members_count is None


def test_dont_containse_count():
    input_json = {
        'id': 111
    }
    input_date = datetime.datetime.now()
    out_group_members_count = create_from_json_with_datetime(input_json, input_date)
    
    assert out_group_members_count is None


def test_containse_other_fields():
    input_json = {
        'id': 111,
        'members_count': 111,
        'other': 'other'
    }
    input_date = datetime.datetime.now()
    group_member_count = GroupMembersCount(count=111, group_id=111, date=input_date)
    output_group_member_count = create_from_json_with_datetime(input_json, input_date)

    assert group_member_count.group_id == output_group_member_count.group_id and \
        group_member_count.count == output_group_member_count.count and \
        group_member_count.date == output_group_member_count.date

