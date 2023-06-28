from flask import Flask
from tree_workshop import tree_mold

app = Flask(__name__)

# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'xyz-pqr'
#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint)


app.register_blueprint(tree_mold, url_prefix="/oak")
app.register_blueprint(tree_mold, url_prefix="/fir")
app.register_blueprint(tree_mold, url_prefix="/ash")

