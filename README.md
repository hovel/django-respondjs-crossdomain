Installation
============

Add *respondjs_crossdomain* into INSTALLED_APPS:

    INSTALLED_APPS = (
        ....
        'respondjs_crossdomain',
    )

Add *respondjs_crossdomain.urls* into urls.py:

    url('', include('respondjs_crossdomain.urls', namespace='respondjs_crossdomain')),

Include *static.html* into base template just before `</head>` tag:

    <head>
        ....
        {% include 'respondjs_crossdomain/static.html' %}
    </head>
