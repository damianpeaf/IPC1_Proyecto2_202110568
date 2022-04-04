from flask import request, jsonify
from api import app
from api import borrow_data
from api.borrowUtils import createNewBorrow, returnBook, searchBorrow


@app.route("/borrow", methods=['POST'])
def createBorrow():

    validationRes = createNewBorrow(request.json)
    response = {}

    if validationRes[0]:
        borrow_data.append(validationRes[0])
        response = {"msg": "Creado correctamente", "status": 200}
    else:
        response = {"msg": "Error", "status": 400, "errors": validationRes[1]}

    # print(borrow_data)

    return jsonify(response)


@app.route("/borrow/<int:id_borrow>", methods=['PUT'])
def returnBorrow(id_borrow):

    validationRes = returnBook(id_borrow)
    response = {}

    if validationRes[0]:
        response = {"msg": "Devuelto correctamente", "status": 200}
    else:
        response = {"msg": "Error", "status": 400, "errors": validationRes[1]}

    # print(borrow_data)

    return jsonify(response)


@app.route("/borrow/<int:id_borrow>", methods=['GET'])
def getBorrow(id_borrow):

    validationRes = searchBorrow(id_borrow)
    response = {}

    if validationRes[0]:
        response = validationRes[0]
    else:
        response = {"msg": "Error", "status": 400, "errors": validationRes[1]}

    # print(borrow_data)

    return jsonify(response)
