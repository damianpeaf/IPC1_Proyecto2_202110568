from flask import request
from api import app
from api import borrow_data
from api.borrowUtils import createNewBorrow

@app.route("/borrow", methods=['POST'])
def createBorrow():

    validationRes = createNewBorrow(request.json)
    response={}

    if validationRes[0]:
        borrow_data.append(validationRes[0])
        response= {"msg": "Creado correctamente","status": 200}
    else:
        response= {"msg": "Error","status": 400, "errors": validationRes[1]}

    print(borrow_data)

    return response