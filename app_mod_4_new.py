from flask import Flask, render_template, abort , jsonify
from model import db

app = Flask(__name__)

# below fxn is used to display home page containing links to all other cards
@app.get("/welcome")
def welcome_fxn():
    cards = db
    return render_template("wel_mod4.html",cards = cards)

# below fxn is used to display the individual card page based on the
# index passed to it
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

# in rest apis : we return the json object from an http server directly instead of the html page 
# returning lists in rest apis in flask are disallowed 
# use jsonify function to return all the cards as a json list 


# convention for rest api's is that the name of the url starts with api
# so at the below url we are returned a json object 
# we have a list of dictionaries and we are returning 1 dictionary below :
@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index]
    
    except IndexError:
        abort(404)


# we are not allowed to serialise a list directly into json response 
# due to security reasons : 

@app.route('/api/cards')
def api_cards_detail():
    return jsonify(db)
