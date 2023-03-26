# line imports the Flask class from the Flask package
from flask import Flask, render_template
from datetime import datetime

# line calls the Flask constructor, which will create a global Flask 
# application object. I pass to the constructor the name of the
#  application, and in most simple cases, you can pass dunder name
#  here, which is a special variable containing the name of the current module
app = Flask(__name__)


# below function is a view function
@app.get("/")
def get_hello():
    return "Hello There !!"


@app.get("/welcome")
def welcome():
    return render_template("welcome.html")


@app.get("/catalog/<string:year>/<string:subject>")
def get_catalog(year, subject):
    return "catalog is ::  year: " + year + "  subject: " + subject


@app.get("/date")
def get_date():
    return "This page was served at : " + str(datetime.now())

# tell Flask in which module our application can be found
# We do this by setting a variable FLASK_APP
# export FLASK_APP=app.py

# windows : 
# set FLASK_APP=app.py


# this tells Flask that we are still developing the application, and it enables some development feature like the debugger
# export FLASK_ENV=development

# ways of running flask app : 
# flask run
# python -m flask run
# flask --debug run

# never create a file with name : flask.py

#  If there's nothing else in the URL, we're visiting the root page for this site, and the name of that page is /


# So, the flow of my application is dictated by the HTTP requests that come in. Any view function I define will only be called if a request is made for the corresponding URL


# export FLASK_ENV=development
#  server now shows that it detects changes and restarts the application automatically.
# So we don't have to restart the server ourselves.
# to see debugger tools we must use : 
# export FLASK_ENV=development
# dont use this when we put this code in production 

# this is added by default : 
# this function will serve any files in the directory called static
# <Rule '/static/<filename>' (OPTIONS, HEAD, GET) -> static>
# and will serve those files under the URL /static, followed by the filename. 

# assumptions : 
# put dynamic html jinja templates in templates folder 
# put css , js , images in the static folder

# there is no connection btw fxn name and url in the app.get decorator
# but generally we can keep them the same
