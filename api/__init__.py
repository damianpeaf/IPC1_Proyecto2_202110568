from flask import Flask

app = Flask(__name__)

users_data=[]

from api import userRoute