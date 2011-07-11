# What If...

What If... is, primarily, a game consisting of a series of linear quizzes. Each quiz
consists of set of tokens and a series of yes or no questions that affect each token
by adding or subtracting a numerical value to them. What If... is also a coding 
exercise using Python, Django and MongoDB. The coding exercise consisted of building
a CMS/Administration to add games, tokens, and questions.

## Python Dependencies

What If... is built using Django with a MongoDB backend. Thus, in order to run the 
application in either a local or remote environment, you'll need the following Python
libraries:

- [django](https://www.djangoproject.com/)
- [pymongo](http://api.mongodb.org/python/current/)
- [mongoengine](http://mongoengine.org/)

If you don't have the dependencies, install them using [easy_install](http://packages.python.org/distribute/easy_install.html)
or [pip](http://www.pip-installer.org/en/latest/index.html).

Additionally, checkout using [virtualenv](http://www.virtualenv.org/en/latest/index.html) 
to manage varying installations and versions of Python and libraries.

## MongoDB

Additionally, you'll need a running instance of MongoDB for the application to work. 
The application in this git repository is configured to connect to an instance of 
MongoDB on the local computer/server.

## Running The Application

Startup MongoDB if you haven't already by calling the mongod command. For example:

    $ sudo /opt/monogodb/bin/mongod

You'll want to first add an initial admin user. Navigate to the project folder and 
execute the custom django 'adduser' command. It will ask you for the user information 
to add to the database. For example:

    $ cd ~/webapps/what-if/whatif
    $ python manage.py adduser
    Username: matt
    Email: matt@nobien.net
    Password: 
    First name: Matt
    Last name: Wright
    User "Matt Wright" successfully added

Start the application by navigating to the project folder and running the django test
server. For example:

    cd ~/webapps/what-if/whatif
    python manage.py runserver 0.0.0.0:8000
