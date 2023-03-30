from flask import Flask,render_template,request,redirect,url_for



app = Flask(__name__)

@app.route('/form',methods = ["GET","POST"])
def form_fxn():
    if request.method == "POST":
        return redirect( url_for('home_fxn') )

    else:
        return render_template("form.html")