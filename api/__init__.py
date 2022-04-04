from flask import Flask

app = Flask(__name__)

users_data = []
books_data = []
borrow_data = []

from api import reporteRoute
from api import borrowRoute
from api import booksRoute
from api import userRoute
