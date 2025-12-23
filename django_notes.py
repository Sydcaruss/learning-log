"""Django - is Python's most popular web framework, a set of tools designed for building interactive web applications."""

"""Creating a virtual environment
# results -> =
Terminal Window -- ll_env/Scripts/activate   = (ll_env)
installing django - pip install django

            Creating a project in django:
            
django-admin startproject ll_project .  # the dot(.) at the end means to create a new project with a directory structure that will make it easy to deploy the app to a server when we are finished developing it. 
    
    Creating the database:
    
python manage.py migrate    # -> anytime we modify a database we say migrating the database.
    
    Viewing the Project
    
python manage.py runserver  # -> runserver command to run the project in its current state
  
                Starting an App
                # A django project is organized group of individual apps that work together to make the project work as a whole.
  
1. activate the virtual environment -> ll_env/Scripts/activate
2. python manage.py startapp learning_logs  #-> startapp appname(learning_logs) the startapp appname tells django to create the infrastructure needed to build an app.
  
    Defining a Model
# Open the file models.py and look at it existing content
# Model tells Django how to work with data that will be stored in the app. A model is a class; it has attributes and methods, just like every class we've discussed.

    Activating Models:
# We have to tell Django include our app in the overall project.
1. Open settings.py (in the ll_project directory); you will see a section that tell Django which apps are installed in the project:
2. Add our app on top of this list by modifying installed apps, for simplicity purpose, groups the apps as default apps and the apps that you are creating.

now: from the terminal->
python manage.py makemigrations learning_logs = Django will be modified with new information related to the model Topic.
# the command makemigrations tells Django to figure out how to modify the database so it can store the data associated with new models we've defined.

The output shows that Django has created a migration file called 0001_initial.py. -> This migration will create a table for the model Topic in the database. - this model will be applied and have Django modify the database:>

python manage.py migrate  -> after this, check the output at the end output line and see where Django confirms that the migration for learning_logs worked OK.

-- Whenever we want to modify the data that Learning Log manages, we'll follow these three steps; modify models.py, call makemigrations on learning_logs, and tell Django to migrate the project.

                The Django Admin Site
Django make it easy to work with your models through its admin site

        Setting a Superuser
Django allows you to create a superuser, a user who has all the privileges available on the site.A user's privileges control the actions they can take.

python manage.py createsuperuser


->to create a superuser: -> username, email address, password


                          Registering a Model with the admin site
                          # Django includes some models in the admin site automatically, such as User and Group, but the models we create need to to added manually.
                          
-> open the admin.py that is in the same directory as models.py ; open admin.py file:

1. import Topic() -> from .models import Topic   # the dot(.) in front tells Django to look for models.py in the same directory as the admin.py.
2. -> admin.site.register(Topic) # -> admin.site.register() tells Django to manage our model through admin site

Now use the superuser account to access the admin site..
 ->http://localhost:8000/admin/   # open this website while you're still have the Django server running!
 
 
    Adding Topics
    
Now that the Topic has been registered with the admin, do your thing and add as many topics as you like.


           Defining Entry Model
# For a user to define what they've been learning about in the topics they've been studying about, we need to define a model for the kinds of entries users can make in their learning logs. Each entry need to be associated with a particular topic.

:The Entry class inherits from Django's base(db) Model class, just as Topic did.
ForeignKey -> is a database term; its a reference to another recode in a database. This is a code that connects each entry to a specific topic.
    on_delete=models.CASCADE -> tells Django that when a topic is deleted, all entries associated with that entry should be deleted as well. This is known as cascading delete.
TextField -> doesn't need to a size limit, because we don't want to limit the size of individuals entries.

                    Migrating the Entry Model
                    
Because we added a new model, we need to migrate the database again.
modify models.py ---> run the command -- python manage.py makemigrations app_name  ---> python manage.py migrate

        Registering Entry with the Admin Site
        
# We also need to register entry the same way we did with Topic on admin.py

                The Django Shell
# Examines data that have been entered programmatically through an interactive terminal session. This interactive terminal is called Django shell and its a great environment for testing and troubleshooting your projects.

python manage.py shell          # > the command manage.py shell, run in active virtual environment, launches a python interpreter that you can use to explore the data stored in your projects database.
from learning_logs.models import Topic
Topic.objects.all()

                    Making Pages: The Learning Home Page
# Making pages with Django consist of three stages: defining URLs, writing views, and writing templates.
URL pattern - describes the way URL is laid out. It also tells Django what to look for when matching a browser request with a site URL, so it knows which page to return.


        Mapping a URL
        
Users requests pages by entering URl into a browser and clicking links, so we need to decide what URLs are needed.
In the main ll_project folder, open the file urls.py. 
> The first two lines import the admin module and the a function to build urls paths.->
from django.contrib import admin
from django.urls import path


> The body of the file defines the urlpatterns variable. In this urls.py file which defines URLs for the project as a whole, the urlpatterns includes set of URLs from the apps in the project.
- The list includes the module admin.site.urls, which defines all urls that can be requested from the admin site.. WE need to add the urls from learning logs>-
=> first we import the include() function and also adding a line to the include module learning_logs.urls-
from django.urls import path, include
=> path('', include('learning_logs.urls')),

----> The default urls.py is in the ll_project folder, now we need to create another one in the learning_logs folder...--> urls.py save it in the learning_logs and write this ff code...

from django.urls import path    # ->  we import the path function which is needed when mapping URLs to views
from  . import views            # the dot(.) tells python to import the views module from the same directory as the current urls.py module
app_name = 'learning_logs'      # the variable app_name helps Django distinguish this urls.py file from the files of the same name in other apps within the project.
urlpatterns = [                 # the variable urlpatterns in this module is a list of individual pages that can be requested for the learning_logs app. The actual url pattern is called to the path() function which takes three arguments.
    # home page
    path('', views.index, name='index'),            # --> the path() function takes three arguments; 1) a string that helps Django route the current request properly. Django receives the requested URL and tries to route the request to a view. 2) specifies which function to call in views.py. 3) provide the name index for this url pattern so we can refer to it more easily in other files throughout the project
    
            Writing a View -- in learning_logs
>- A view function takes in information from a request, prepares the data needed to generate a page, and then sends the data back to the browser. It often does this by using template that defines what the page will look like.

>> The render () function imported here renders the data the response based on the data provided by views.

=> def index(request):
        # The home page for the learning log
        return render(request, 'learning_logs/index.html')      # The render() function here passes two arguments: the original request object and a template it can use to build the page.
 
 
                    Writing a Template
    # A template defines what a page looks like and Django fills in the relevant data each the page is requested. A template allows you to access any data provided by the view.
    
Inside learning_logs folder, mk a new dir called templates. Inside templates, make another dir called learning_logs. Inside inner learning_logs dir, mk a new file called index.html
 
 
            Building Additional Pages
        
        Template Inheritance
Creating a base template that will be directly into each page

    The Parent Template
We'll create a template called a base.html in the same dir as index.html. This file will contain elements common to all pages; every other template will inherit from base.html

<p> 
  <a href="{% 'learning_logs:index' %}">Learning Log</a>
  </p>
  
  {% block content %}{% endblock content %}
  
    The Child Template
Rewrite index.html to inherit from base.html

{% extends 'learning_logs/base.html' %}         # A child template must have an {% extends %} tag on the first line to tell Django which parent template to inherit from.

{% block content %}                             # We define the content block by inserting a {% block %} tag with name content. Everything we not inheriting from the parent template goes inside the content block.
...................all the contents
{% endblock content %}                          # this tag indicate that we are finished defining the content by using an {% endblock content %}



"""