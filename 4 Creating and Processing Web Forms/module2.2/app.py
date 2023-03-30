from flask import Flask,render_template,request,redirect,url_for

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"

class NewItemForm(FlaskForm):
    # Name is label of the field 
    s_name = StringField("Name")
    s_rollno = StringField("Roll Number")
    submit = SubmitField("Submit")

@app.route('/new_item',methods = ["GET","POST"])
def new_item_fxn():
    if request.method == "POST":
        return render_template("home.html")

    else:
        form_obj  = NewItemForm()
        return render_template("form.html",form= form_obj)
    