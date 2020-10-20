#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/10/20
@Author  : dilless
@Site    : 
@File    : routing
@Software: PyCharm
"""
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]
