# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os.path import realpath, dirname, join

from django.http import HttpResponse, HttpResponseNotFound


APP_ROOT = dirname(realpath(__file__))


def static(request, type):
    if type == 'img':
        filename = 'respond.proxy.gif'
        content_type = 'image/gif'
    elif type == 'js':
        filename = 'respond.proxy.js'
        content_type = 'application/javascript'
    else:
        print('Wrong file type. Expected "img" or "js".')
        return HttpResponseNotFound()

    try:
        with open(join(APP_ROOT, 'static', filename), 'rb') as file:
            return HttpResponse(file.read(), content_type=content_type)
    except IOError:
        print('{} not found.'.format(filename))
        return HttpResponseNotFound()
