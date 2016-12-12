- Creating an app in project
    python manage.py startapp [app_label]
    python manage.py startapp main

- Running project
    python manage.py runserver

- Run a migration once updated model
    - Create the migration:
        python manage.py makemigrations

    - Apply migration to the database:
        python manage.py migrate

- Using Django Shell
    - Using Django interactive shell allows us to create objects in our model as well as query our model.
        python manage.py shell

    - Create Location objects and query Location model:
        from main.models import Location
        location = Location(name='The Delicate Arch, UT', predators='Scorpions', num_restaurants=0, img_url='http://courseware.codeschool.com/try_django/images/delicate-arch.jpg')
        location.save()
        Location.objects.all()
