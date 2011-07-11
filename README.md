# What If...

What If... is, primarily, a game consisting of a series of linear quizzes. Each quiz
consists of set of tokens and a series of yes or no questions that affect each token
by adding or subtracting a numerical value to them. What If... is also a coding 
exercise using Python, Django and MongoDB. The coding exercise consisted of building
a CMS/Administration area and a presentation UI for users to play the games.

## Python Dependencies

What If... is built using Django with a MongoDB backend. Thus, in order to run the 
application in either a local or remote environment, you'll need the following Python
libraries:

- [django](https://www.djangoproject.com/)
- [pymongo](http://api.mongodb.org/python/current/)
- [mongoengine](http://mongoengine.org/)

If you don't have the dependencies, install them using [easy_install](http://packages.python.org/distribute/easy_install.html)
or [pip](http://www.pip-installer.org/en/latest/index.html). Additionally, checkout using [virtualenv](http://www.virtualenv.org/en/latest/index.html) 
to manage varying installations and versions of Python and libraries.

## MongoDB

The application is built using [MongoDB](http://www.mongodb.org/). In addition, it uses
a handy MongoDB object mapper called mongoengine, as mentioned above. The traditional 
django model classes do not exist and instead the model classes are defined in the 
/whatif/games/documents.py file.
 
You'll need a running instance of MongoDB for the application to work. The application 
in this git repository is configured to connect to an instance of MongoDB on the local 
computer/server. Thus, you'll need to install MongoDB on your computer or the server 
the applicaiton will run on. There is a [great tutorial}(http://library.linode.com/databases/mongodb/ubuntu-10.04-lucid)
 on how to install and configure MongoDB for Linux on Linode's website.


## Running The Application

If you haven't already, clone the project repository into a convenient folder on your
computer or server. For example:

    $ cd ~/
    $ mkdir webapps
    $ cd webapps
    $ git clone git@github.com:mattupstate/what-if.git

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

Now you should be good to go. Now you'll want to head into the admin area and add some 
games, tokens and questions. Now get to it!
