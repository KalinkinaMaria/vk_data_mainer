"""
Tests for transtation json to Group
"""

import pytest

from database.model.group import Group
from translator.group_translator import create_from_json_with_link


def test_correct():
    input_json = {
        'id': 111,
        'screen_name': 'test'
    }
    input_link = 'vk.com/test'
    correct_group = Group(id=111, name='test', link='vk.com/test')
    out_group = create_from_json_with_link(input_json, input_link)
    
    assert out_group.id == correct_group.id and \
        out_group.name == correct_group.name and \
        out_group.link == correct_group.link


def test_json_is_none():
    input_json = None
    input_link = 'vk.com/test'
    out_group = create_from_json_with_link(input_json, input_link)
    
    assert out_group is None


def test_link_is_none():
    input_json = {
        'id': 111,
        'screen_name': 'test'
    }
    input_link = None
    out_group = create_from_json_with_link(input_json, input_link)
    
    assert out_group is None


def test_json_is_none_and_link_is_none():
    input_json = None
    input_link = None
    out_group = create_from_json_with_link(input_json, input_link)
    
    assert out_group is None


def test_dont_containse_id():
    input_json = {
        'screen_name': 'test'
    }
    input_link = 'vk.com/test'
    out_group = create_from_json_with_link(input_json, input_link)
    
    assert out_group is None


def test_dont_containse_name():
    input_json = {
        'id': 111,
    }
    input_link = 'vk.com/test'
    out_group = create_from_json_with_link(input_json, input_link)
    
    assert out_group is None


def test_containse_other_fields():
    input_json = {
        'id': 111,
        'screen_name': 'test',
        'other': 'other'
    }
    input_link = 'vk.com/test'
    correct_group = Group(id=111, name='test', link='vk.com/test')
    out_group = create_from_json_with_link(input_json, input_link)
    
    assert out_group.id == correct_group.id and \
        out_group.name == correct_group.name and \
        out_group.link == correct_group.link
