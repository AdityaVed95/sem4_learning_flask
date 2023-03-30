from flask import Flask,render_template,request,redirect,url_for
import get_data_from_db
from flask_wtf import FlaskForm

app = Flask(__name__)

@app.route('/home')
def home_fxn():
    return render_template("home.html")

# used to include a css file in the html file
# this fxn sends back the css file
@app.route("/static_content/<filename>")
def static_content_fxn(filename):
    return send_from_directory("static",filename)

@app.route("/get_data")
def get_data_fxn():
    
    operation_result = get_data_from_db.select_from_students_db()
    return operation_result
    



