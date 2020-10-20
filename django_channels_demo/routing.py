#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/10/20
@Author  : dilless
@Site    : 
@File    : routing
@Software: PyCharm
"""
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import chat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns,
        )
    )
})
