from flask import Flask

app = Flask(__name__)

users_data=[]
books_data=[]

from api import userRoute
from api import booksRoute
