from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)

users_data = []
books_data = []
borrow_data = []

@app.errorhandler(404)
def handle_404(e):
    return {'errors':[]}

from api import reporteRoute
from api import borrowRoute
from api import booksRoute
from api import userRoute
