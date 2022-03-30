from api import app

@app.route("/")
def hello_world():
    return "<p>Hola Mundo!</p>"