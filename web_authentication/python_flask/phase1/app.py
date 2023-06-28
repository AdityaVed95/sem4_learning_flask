from flask import Flask, render_template, redirect, request, session ,flash
from flask_session import Session

# session and Session are application level sessions

app = Flask(__name__)
app.secret_key = 'xyz'

# configuring session object
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
# calling a constructor of Session class and passing app as an object to it
Session(app)


# for every http connection there is a session established
# since every session is unique  
# any object in that will be unique to that session

# for every unique (client-server pair) connection : a dictionary
#  object called session is created
# 

@app.get("/")
def index():
    if ("name" in session.keys()):
        # here the session exists at both the network level and the 
        # applicaiton level 
        print(session['name'])
    else:
        # here the session has been established at the network level but not 
        # at the application level 
        print("name not present")

    if not session.get("name"):
        return redirect("/login")

    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # record the user name
        session["name"] = request.form.get("name")
        # redirect to the main page
        flash('Login successful!')
        

    return render_template("login.html")


# session is a dictionary

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")


@app.route("/myprofile")
def my_profile():
    if not session.get("name"):
        return redirect("/login")
    profile = "Please create profile at LinkedIn-> your LinkedINURL is .. (get this url from database..)"
    return render_template('my_profile.html', profile=profile)


if __name__ == "__main__":
    app.run(debug=True)
