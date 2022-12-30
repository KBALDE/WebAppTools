# Django A Quick Overview

Django is a Python framework that makes it easier to create web sites using Python.

Django takes care of the difficult stuff so that you can concentrate on building your web applications.

Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).

Django follows the MVT design pattern (Model View Template).

**Model** - The data you want to present, usually data from a database.
**View** - A request handler that returns the relevant template and content - based on the request from the user.
**Template** - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.


## Model
The model provides data from the database.

In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases.

The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it.

Django, with ORM, makes it easier to communicate with the database, without having to write complex SQL statements.

The models are usually located in a file called **models.py**.


## View
A view is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the final result.

The views are usually located in a file called **views.py**.

## Template
A template is a file where you describe how the result should be represented.

Templates are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other results, but we will concentrate on .html files.

Django uses standard HTML to describe the layout, but uses Django tags to add logic:
```php
<h1>My Homepage</h1>

<p>My name is {{ firstname }}.</p>

```
The templates of an application is located in a folder named **templates**.

## URLs
Django also provides a way to navigate around the different pages in a website.

When a user requests a URL, Django decides which view it will send it to.

This is done in a file called **urls.py**.

## What Django does 

When you have installed Django and created your first Django web application, and the browser requests the URL, this is basically what happens:

- Django receives the URL, checks the urls.py file, and calls the view that matches the URL.
- The view, located in views.py, checks for relevant models.
- The models are imported from the models.py file.
- The view then sends the data to a specified template in the template folder.
- The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.

Django can do a lot more than this, but this is basically what you will learn in this tutorial, and are the basic steps in a simple web application made with Django.


## Django Create Project

It is better to run qyour project in a virtual environment

```sh
conda create -n my_project_venv python=3.8 anaconda
# and then activate the venv
conda activate my_project_venv

```


## My First Project
Once you have come up with a suitable name for your Django project, like mine: **my_tennis_club**, navigate to where in the file system you want to store the code (in the virtual environment), I will navigate to the **my_project_venv** folder, and run this command in the command prompt:

```sh
django-admin startproject my_tennis_club
```
Django creates a my_tennis_club folder on my computer, with this content:

```
my_tennis_club
    manage.py
    my_tennis_club/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
```

## Run the Django Project
Now that you have a Django project, you can run it, and see what it looks like in a browser.

Navigate to the /my_tennis_club folder and execute this command in the command prompt:

```sh
python manage.py runserver
```

## What is an App?
An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.

In this tutorial we will create an app that allows us to list and register members in a database.

But first, let's just create a simple Django app that displays "Hello World!".

## Create App
I will name my app members.

Start by navigating to the selected location where you want to store the app, in my case the my_tennis_club folder, and run the command below.

If the server is still running, and you are not able to write commands, press [CTRL] [BREAK], or [CTRL] [C] to stop the server and you should be back in the virtual environment.

```py
py manage.py startapp members
```

Django creates a folder named members in my project, with this content:

```sh
my_tennis_club
    manage.py
    my_tennis_club/
    members/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
```

## Views
Django views are Python functions that takes http requests and returns http response, like HTML documents.

A web page that uses Django is full of views with different tasks and missions.

Views are usually put in a file called **views.py** located on your app's folder.

There is a views.py in your members folder that looks like this:

Modify it like below :

```py
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

```

## URLs
Create a file named urls.py in the same folder as the views.py file, and type this code in it:


```py
# my_tennis_club/members/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
```

The **urls.py** file you just created is specific for the members application. We have to do some routing in the root directory **my_tennis_club** as well. This may seem complicated, but for now, just follow the instructions below.

There is a file called urls.py on the **my_tennis_club** folder, open that file and add the **include** module in the **import statement**, and also add a **path()** function in the **urlpatterns[]** list, with arguments that will route users that comes in via 127.0.0.1:8000/.

Then your file will look like this:

```py
# my_tennis_club/my_tennis_club/urls.py:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]
```


## Templates
We learned that the result should be in HTML, and it should be created in a template, so let's do that.

Create a templates folder inside the members folder, and create a HTML file named myfirst.html.

The file structure should be like this:
```sh
my_tennis_club
    manage.py
    my_tennis_club/
    members/
        templates/
            myfirst.html
```

Open the HTML file and insert the following `my_tennis_club/members/templates/myfirst.html`:

```php
<!DOCTYPE html>
<html>
<body>

<h1>Hello World!</h1>
<p>Welcome to my first Django project!</p>

</body>
</html>

```

## Modify the View
Open the views.py file and replace the members view with this:

```py
# my_tennis_club/members/views.py:
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
```

## Change Settings
To be able to work with more complicated stuff than "Hello World!", We have to tell Django that a new app is created.

This is done in the settings.py file in the my_tennis_club folder.

Look up the INSTALLED_APPS[] list and add the members app like this:

```py
my_tennis_club/my_tennis_club/settings.py:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members'
]
```

Then run this command:
```py
python manage migrate
```

Now you can start the server 
```
python manage.py runserver
```

## Django Models

Django Model is a table in your database.

Up until now in this tutorial, output has been static data from Python or HTML templates.

Now we will see how Django allows us to work with data, without having to change or upload files in the prosess.

In Django, data is created in objects, called Models, and is actually tables in a database.

## Create Table (Model)
To create a model, navigate to the models.py file in the /members/ folder.

Open it, and add a Member table by creating a Member class, and describe the table fields in it:

```py
# my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

```

The first field, firstname, is a Text field, and will contain the first name of the members.

The second field, lastname, is also a Text field, with the member's last name.

Both firstname and lastname is set up to have a maximum of 255 characters.



## Migrate
Now when we have described a Model in the models.py file, we must run a command to actually create the table in the database.

Navigate to the /my_tennis_club/ folder and run this command:

```sh
python manage.py makemigrations
```
Django creates a file describing the changes and stores the file in the **/migrations/** folder:

```py
my_tennis_club/members/migrations/0001_initial.py:

# Generated by Django 4.1.2 on 2022-10-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
    ]

```

Note that Django inserts an **id** field for your tables, which is an auto increment number (first record gets the value 1, the second record 2 etc.), this is the default behavior of Django, you can override it by describing your own id field.

The table is not created yet, you will have to run one more command, then Django will create and execute an SQL statement, based on the content of the new file in the /migrations/ folder.

Run the migrate command:
```sh
py manage.py migrate
```

## Add Records
The Members table created in the previous chapter is empty.

We will use the Python interpreter (Python shell) to add some members to it.

To open a Python shell, type this command:

```sh
py manage.py shell
```
Now we are in shell mode

```sh

from members.models import Member
 Member.objects.all()
# This should give you an empty QuerySet object, like this:
# <QuerySet []>
## A QuerySet is a collection of data from a database.

# Add a record to the table, by executing these two lines:
member = Member(firstname='Emil', lastname='Refsnes')
member.save()

# Execute this command to see if the Member table got a member:
 Member.objects.all().values()
```
## Add Multiple Records
You can add multiple records by making a list of Member objects, and execute .save() on each entry:

```py
member1 = Member(firstname='Tobias', lastname='Refsnes')
member2 = Member(firstname='Linus', lastname='Refsnes')
member3 = Member(firstname='Lene', lastname='Refsnes')
member4 = Member(firstname='Stale', lastname='Refsnes')
member5 = Member(firstname='Jane', lastname='Doe')
members_list = [member1, member2, member3, member4, member5]
for x in members_list:
	x.save()

Member.objects.all().values()

#<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
#{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
#{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
#{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
#{'id': 5, 'firstname': 'Stale', 'lastname': 'Refsnes'},
#{'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]>

```

## Update Records
To update records that are already in the database, we first have to get the record we want to update:
```py
from members.models import Member
x = Member.objects.all()[4]

# x will now represent the member at index 4, which is "Stale Refsnes", but to make sure, let us see if that is correct:
# Now we can change the values of this record:
x.firstname = "Stalikken"
x.save()

# Execute this command to see if the Member table got updated:
Member.objects.all().values()
```
## Delete Records
To delete a record in a table, start by getting the record you want to delete:
```py
from members.models import Member
x = Member.objects.all()[5]
# x will now represent the member at index 5, which is "Jane Doe", but to make sure, let us see if that is correct:
# Now we can delete the record:
x.delete()

# to display the left members
Member.objects.all().values()

```

## Add Fields in the Model
To add a field to a table after it is created, open the models.py file, and make your changes:

```py
#my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField()
  joined_date = models.DateField()

```
As you can see, we want to add phone and joined_date to our Member Model.

This is a change in the Model's structure, and therefor we have to make a migration to tell Django that it has to update the database:

```sh
py manage.py makemigrations members
```

Which, in my case, will result in a prompt, because I try to add fields that are not allowed to be null, to a table that already contains records.

As you can see, Django asks if I want to provide the fields with a specific value, or if I want to stop the migration and fix it in the model:

I will select option 2, and open the models.py file again and allow NULL values for the two new fields:
```py
my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
```
And make the migration once again
```sh
py manage.py makemigrations members

# Run the migrate command:
py manage.py migrate
```






