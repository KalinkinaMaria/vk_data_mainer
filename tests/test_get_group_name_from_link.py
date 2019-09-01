import pytest

from manager import get_group_name_from_link


def test_empty_link():
    link = ""
    correct_group = ""

    assert get_group_name_from_link(link) == correct_group


def test_correct_link():
    link = "http://vk.com/test_group"
    correct_group = "test_group"

    assert get_group_name_from_link(link) == correct_group


def test_without_scheme():
    link = "vk.com/test_group"
    correct_group = "test_group"

    assert get_group_name_from_link(link) == correct_group


def test_link_with_vkontakte():
    link = "http://vkontakte.ru/test_group"
    correct_group = "test_group"

    assert get_group_name_from_link(link) == correct_group


def test_only_hostname():
    link = "http://vk.com/"
    correct_group = ""

    assert get_group_name_from_link(link) == correct_group


def test_not_group_link():
    link = "http://vkontakte.ru/test_group/page"
    correct_group = ""

    assert get_group_name_from_link(link) == correct_group


def test_link_ends_with_slash():
    link = "http://vk.com/test_group/"
    correct_group = "test_group"

    assert get_group_name_from_link(link) == correct_group