==============
app - worldmap
==============

app is a Django app to conduct web-based worldwide map. it lists out all continents,
countries, states


Quick start
-----------

1. Add "app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "app",
    ]

2. Include the app URLconf in your project urls.py like this::

    path("app/", include("app.urls")),

3. Run ``python manage.py migrate`` to create the app models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/app/ to participate in the worldmap.