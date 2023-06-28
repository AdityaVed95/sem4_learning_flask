from flask import Flask,request
import smtplib

app = Flask(__name__)

@app.route('/form',methods=["GET","POST"])
def form_fxn():
    message = "You have been subscribed to my website"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("ady.ved@gmail.com","bzuvtweknpsnjjbt") # sender
    server.sendmail("ady.ved@gmail.com", "rugvedpalodkar2204@gmail.com" , message) # sender , reciever
    return ("done")
