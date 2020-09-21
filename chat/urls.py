#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/9/21
@Author  : dilless
@Site    : 
@File    : urls
@Software: PyCharm
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
