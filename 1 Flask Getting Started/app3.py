# model template view 
# aka model view controller

# mtv or mvc

# export FLASK_APP=app3.py

from flask import Flask , render_template , abort
from model import db


app = Flask(__name__)

@app.get("/")
def main_run():
    return render_template("welcome.html",
    
    message = "This is our message from a view"

    )



@app.get("/cards")
def cards_fxn():
    card_from_db = db[0]
    return render_template("cards_templates.html",

    card = card_from_db ,
    type_of_db = type(db), 
    type_of_card = type(card_from_db),
    # type_of_card_0 = type(card.question)



    
    )
 

@app.get('/cards_fetch/<int:index>')
def cards_fetch_fxn(index):
    try:
        card_from_db = db[index]
        return render_template("new_cards_template.html",card = card_from_db)
    except IndexError:
        abort(404)
        # return "Array index out of bound"

# below is a list 
# it is db
#  [
#         {
#         "question": "Hello (formal)",
#         "answer": "Здравствуйте"
#         },
#         {
#         "question": "Goodbye (formal)",
#         "answer": "До свидания"
#         },
#         {
#         "question": "Hello (informal)",
#         "answer": "Привет"
#         },
#         {
#         "question": "Goodbye (informal)",
#         "answer": "Пока"
#         }
#     ]

# this is dictionary :
# this is card_from_db i.e db[0]

# {
#     "question": "Hello (formal)",
#     "answer": "Здравствуйте"
# }
