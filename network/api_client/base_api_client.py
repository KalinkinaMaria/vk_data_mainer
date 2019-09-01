"""
Base module for vk api
"""

import vk

import setting

session = vk.Session(setting.VK_SERVICE_KEY)
api = vk.API(session)