from flask import Flask, render_template, abort , jsonify , request , redirect , url_for
from model import db , save_db


app = Flask(__name__)


@app.get("/welcome")
def welcome_fxn():
    cards = db
    return render_template("wel_mod4.html",cards = cards)

@app.get("/cards_fetch/<int:index_from_db>")
def cards_fetch_fxn(index_from_db):
    try:
        card_from_db = db[index_from_db]
        return render_template("cards_module_4_template.html", 
        card=card_from_db, 
        index=index_from_db,
        max_index=len(db)-1)
# for 4 dictionaries in list  :
# max_index value is 3
    except IndexError:
        abort(404)


@app.route('/add_card',methods = ["GET","POST"])
def add_card_fxn():
    if request.method == "POST":
        # form has been submitted , we now process the data 
        card = {"question" : request.form['question'], "answer" : request.form['answer']}
        # "question" is the key of the dictionary 
        # 'question' is the value returned from the form , name of that value is 'question'
        db.append(card)
        save_db()
        return redirect( url_for('cards_fetch_fxn',index_from_db = len(db)-1) )
        
    else:
        # 1st time when the user visits the website : 
        return render_template('add_card_template.html')


@app.route('/remove_card/<int:index_from_user>',methods = ["GET","POST"])
def remove_card_fxn(index_from_user):
    try:
        if request.method=="POST":
            db.pop(index_from_user)
            # or use : del db[index]
            save_db()
            return redirect(url_for('welcome_fxn'))

        else:
            card_from_db = db[index_from_user]
            return render_template('remove_card_template.html',card = card_from_db)

    except IndexError:
        abort(404)


# app 6 :
@app.get('/welcome_mod6')
def welcome_mod6_fxn():
    cards = db
    return render_template("wel_mod6.html",cards = cards)


