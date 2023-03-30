from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/home')
def home_fxn():
    return render_template("home.html")

@app.route('/form',methods = ["GET","POST"])
def form_fxn():
    # default is get when the browser request server for web page
    # if we dont use if else , then by default will be get 
    if request.method == "POST":
        # print(type(request))
        # request is an object like a dictionary but not exactly a dictionary
        return redirect(url_for('home_fxn'))
        
        # use above line or : 
        # return redirect( url_for('home_fxn') )

    else:
        return render_template("form.html")

@app.route('/form_handle',methods = ["GET","POST"])
def form_handle_fxn():
    if request.method == "POST":
        return render_template("home.html")

