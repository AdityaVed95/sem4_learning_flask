from flask import Flask
from datetime import datetime

app = Flask(__name__)

counter = 0


@app.get("/")
def count_call():
    global counter
    counter +=1
    return "This website is called for " + str(counter) + " times"
    
@app.get("/new")
def count_call1():
    global counter
    counter +=1
    return "This website is called for " + str(counter) + " times"

# below code generates this error : 
# AssertionError: View function mapping is overwriting an existing endpoint 
# function: count_call1
# @app.get("/new1")
# def count_call1():
#     global counter
#     counter +=1
#     return "This website is called for " + str(counter) + " times"

# so we cant have more than one functions with the same name in the same file 


# in order to see the mapping of api end point and the function being called 
# at that end point : use this command in python repl: 
# import app2
# app2.app.url_map
