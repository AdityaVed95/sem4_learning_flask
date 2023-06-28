from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from insert_student import insert_student_into_db

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.get("/signup", methods=["POST", "GET"])
def signup_fxn():
    if request.method == "POST":
        session['studentName'] = request.form.get("studentName")
        insert_student_into_db(request.form.get("studentId"),request.form.get("rollNo"),request.form.get("studentName"),request.form.get("studentEmail"),request.form.get("studentPassword"),request.form.get("studentCurrentSem"),request.form.get("deptId"))
        
        # studentId,rollNo,studentName,studentEmail,studentPassword,studentCurrentSem,deptId
    else:
        return render_template("signup.html")



