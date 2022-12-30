## Create Template
After creating Models, with the fields and data we want in them, it is time to display the data in a web page.

Start by creating an HTML file named all_members.html and place it in the /templates/ folder:

```php
<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>
  
<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }} {{ x.lastname }}</li>
  {% endfor %}
</ul>

</body>
</html>
```

Do you see the {% %} brackets inside the HTML document?

They are Django Tags, telling Django to perform some programming logic inside these brackets.

## Modify View
Next we need to make the model data available in the template. This is done in the view.

In the view we have to import the Member model, and send it to the template like this:

```py
# my_tennis_club/members/views.py:
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
```

The members view does the following:

- Creates a **mymembers** object with all the values of the Member model.
- Loads the **all_members.html** template.
- Creates an object containing the **mymembers **object.
- Sends the object to the template.
- Outputs the HTML that is rendered by the template.


## Details Template
The next step in our web page will be to add a Details page, where we can list more details about a specific member.

Start by creating a new template called details.html:

my_tennis_club/members/templates/details.html:
```php
<!DOCTYPE html>
<html>

<body>

<h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>
  
<p>Phone: {{ mymember.phone }}</p>
<p>Member since: {{ mymember.joined_date }}</p>

<p>Back to <a href="/members">Members</a></p>

</body>
</html>
```

## Add Link in all-members Template
The list in all_members.html should be clickable, and take you to the details page with the ID of the member you clicked on:

my_tennis_club/members/templates/all_members.html:

```php
<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>
  
<ul>
  {% for x in mymembers %}
    <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
  {% endfor %}
</ul>

</body>
</html>
```

## Create new View
Then create a new view in the views.py file, that will deal with incoming requests to the /details/ url:

```py
# my_tennis_club/members/views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request)
```

The details view does the following:

- Gets the id as an argument.
- Uses the id to locate the correct record in the Member table.
- loads the details.html template.
- Creates an object containing the member.
- Sends the object to the template.
- Outputs the HTML that is rendered by the template.

## Add URLs
Now we need to make sure that the /details/ url points to the correct view, with id as a parameter.

Open the urls.py file and add the details view to the urlpatterns list:

my_tennis_club/members/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
```

## The extends Tag
In the previous pages we created two templates, one for listing all members, and one for details about a member.

The templates have a set of HTML code that are the same for both templates.

Django provides a way of making a "parent template" that you can include in all pages to for the stuff that are the same in all pages.

Start by creating a template called master.html, with all the necessary HTML elements:

### Master
my_tennis_club/members/templates/master.html:
```php
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
</head>
<body>

{% block content %}
{% endblock %}

</body>
</html>
```
Do you see Django block Tag inside the <title> element, and the <body> element?

They are placeholders, telling Django to replace this block with content from other sources.

### Modify Templates
Now the two templates (all_members.html and details.html) can use this master.html template.

This is done by including the master template with the {% extends %} tag, and inserting a title block and a content block:
### Members
```php
{% extends "master.html" %}

{% block title %}
  My Tennis Club - List of all members
{% endblock %}


{% block content %}
  <h1>Members</h1>
  
  <ul>
    {% for x in mymembers %}
      <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```
### Details
```php
{% extends "master.html" %}

{% block title %}
  Details about {{ mymember.firstname }} {{ mymember.lastname }}
{% endblock %}


{% block content %}
  <h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>
  
  <p>Phone {{ mymember.phone }}</p>
  <p>Member since: {{ mymember.joined_date }}</p>
  
  <p>Back to <a href="/members">Members</a></p>
  
{% endblock %}
```

## Main Index Page
Our project needs a main page.

The main page will be the landing page when somene visits the root folder of the project.

Now, you get an error when visiting the root folder of your project:

my_tennis_club/members/templates/main.html:

### Main

```php
{% extends "master.html" %}

{% block title %}
  My Tennis Club
{% endblock %}


{% block content %}
  <h1>My Tennis Club</h1>

  <h3>Members</h3>
  
  <p>Check out all our <a href="members/">members</a></p>
  
{% endblock %}
```

## Create new View
Then create a new view called main, that will deal with incoming requests to root of the project:
```py
# my_tennis_club/members/views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

```

The main view does the following:
- loads the main.html template.
- Outputs the HTML that is rendered by the template.

## Add URL
Now we need to make sure that the root url points to the correct view.

Open the urls.py file and add the main view to the urlpatterns list:

```py
# my_tennis_club/members/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
```
## Add Link Back to Main
The members page is missing a link back to the main page, so let us add that in the all_members.html template, in the content block:
```php
{% extends "master.html" %}

{% block title %}
  My Tennis Club - List of all members
{% endblock %}


{% block content %}

  <p><a href="/">HOME</a></p>

  <h1>Members</h1>
  
  <ul>
    {% for x in mymembers %}
      <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```


## Include Member in the Admin Interface

To include the Member model in the admin interface, we have to tell Django that this model should be visible in the admin interface.

This is done in a file called admin.py, and is located in your app's folder, which in our case is the members folder.

Open it, and it should look like this:

```py
# my_tennis_club/members/admin.py:

from django.contrib import admin
from .models import Member

# Register your models here.
admin.site.register(Member)
```

## Change the String Representation
To change the string representation, we have to define the __str__() function of the Member Model in models.py, like this:

```py
#my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
```


## Django Template Variables

In Django templates, you can render variables by putting them inside ``{{ }}`` brackets:

```php
<h1>Hello {{ firstname }}, how are you?</h1>
```

## Create Variable in View
The variable firstname in the example above was sent to the template via a view:

```py
# views.py:

from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  # the variable is the key here
  context = {
    'firstname': 'Linus',
  }
  
  return HttpResponse(template.render(context, request))
```
As you can see in the view above, we create an object named context and fill it with data, and send it as the first parameter in the template.render() function.

## Create Variables in Template
You can also create variables directly in the template, by using the {% with %} template tag:
templates/template.html:

```php
{% with firstname="Tobias" %}
<h1>Hello {{ firstname }}, how are you?</h1>
```
## Data From a Model
The example above showed a easy approach on how to create and use variables in a template.

Normally, most of the external data you want to use in a template, comes from a **model**.

We have created a model in the previous chapters, called Member, which we will use in many examples in the next chapters of this tutorial.

To get data from the Member model, we will have to import it in the **views.py** file, and extract data from it in the view:

```py
# members/views.py:

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

def testing(request):
  mymembers = Member.objects.all().values()

  template = loader.get_template('template.html')
  
  context = {
    'mymembers': mymembers,
  }
  
  return HttpResponse(template.render(context, request))
```

Now we can use the data in the template:

templates/template.html:

```php
<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>
```
## Template Tags
In Django templates, you can perform programming logic like executing if statements and for loops.

These keywords, **if** and **for**, are called "template tags" in Django.

To execute template tags, we surround them in {% %} brackets.

```php
{% if greeting == 1 %}
  <h1>Hello</h1>
{% else %}
  <h1>Bye</h1>
{% endif %}
```

## Django Code
The template tags are a way of telling Django that here comes something else than plain HTML.

The template tags allows us to to do some programming on the server before sending HTML to the client.
```php
<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>

```
For more information on tags click [here](https://www.w3schools.com/django/django_template_tags.php)

autoescape	Specifies if autoescape mode is on or off
block		Specifies a block section
comment		Specifies a comment section
csrf_token	Protects forms from Cross Site Request Forgeries
cycle		Specifies content to use in each cycle of a loop
debug		Specifies debugging information
extends		Specifies a parent template
filter		Filters content before returning it
firstof		Returns the first not empty variable
for			Specifies a for loop
if			Specifies a if statement
ifchanged	Used in for loops. Outputs a block only if a value has changed since the last iteration
include		Specifies included content/template
load		Loads template tags from another library
lorem		Outputs random text
now			Outputs the current date/time
regroup		Sorts an object by a group
resetcycle	Used in cycles. Resets the cycle
spaceless	Removes whitespace between HTML tags
templatetag	Outputs a specified template tag
url	Returns the absolute URL part of a URL
verbatim	Specifies contents that should not be rendered by the template engine
widthratio	Calculates a width value based on the ratio between a given value and a max value
with		Specifies a variable to use in the block

## Django Include Tag

The include tag allows you to include a template inside the current template.

This is useful when you have a block of content that is the same for many pages.

```php
<h1>Hello</h1>

<p>This page contains a footer in a template.</p>

{% include 'footer.html' %} 
```

## Variables in Include
You can send variables into the template by using the with keyword.

In the include file, you refer to the variables by using the {{ variablename }} syntax:

```php
<!DOCTYPE html>
<html>
<body>

{% include "mymenu.html" with me="TOBIAS" sponsor="W3SCHOOLS" %}

<h1>Welcome</h1>

<p>This is my webpage</p>

</body>
```



















