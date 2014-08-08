# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from respondjs_crossdomain.views import static

urlpatterns = patterns(
    '',
    url('^respond\.proxy\.gif$', static, {'type': 'img'}, name='static-img'),
    url('^respond\.proxy\.js$', static, {'type': 'js'}, name='static-js'),
)
