from flask import Flask , render_template , abort
from model import db

app = Flask(__name__)

@app.get("/welcome")
def welcome():
    return render_template("welcome.html")

# @app.get('/cards_fetch/<int:index>')
# def cards_fetch_fxn(index):
#     try:
#         card_from_db = db[index]
#         return render_template("cards_module_4_template.html",card=card_from_db)
#     except IndexError:
#         abort(404)

@app.get("/cards_fetch/<int:index_from_db>")
def cards_fetch_fxn(index_from_db):
    try:
        card_from_db = db[index_from_db]
        return render_template("cards_module_4_template.html",card = card_from_db,index = index_from_db)
    except IndexError:
        abort(404)

