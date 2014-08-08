Installation
============

Add *respondjs_crossdomain* into INSTALLED_APPS:

    INSTALLED_APPS = (
        ....
        'respondjs_crossdomain',
    )

Add *respondjs_crossdomain.urls* into urls.py:

    url('', include('respondjs_crossdomain.urls', namespace='respondjs_crossdomain')),

Include static template into base template. If you use *django.contrib.staticfiles* include `staticfiles.html`:

    <head>
        ....
        {% include 'respondjs_crossdomain/staticfiles.html' %}
    </head>

or if you use built-in *static* tag include `static.html`:

    <head>
        ....
        {% include 'respondjs_crossdomain/static.html' %}
    </head>
