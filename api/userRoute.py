
from flask import request, jsonify
from api import app
from api import users_data
from api.userUtils import validateUserData, updateUserFields, searchUser


# Propiedades usuario
# Id: identificador alfanumérico.
# Name: nombre y apellido del usuario.
# Nickname: álias del usuario.
# Password: contraseña del usuario.
# Rol: puede ser “Estudiante” o “Catedrático”.
# Available: valor booleano que indica si el usuario está o no habilitado para realizar préstamos.


@app.route("/user", methods=['POST'])
def createUsser():

    validationRes = validateUserData(request.json)
    response = {}

    if validationRes[0]:
        users_data.append(validationRes[0])
        response = {"msg": "Creado correctamente", "status": 200}
    else:
        response = {"msg": "Error", "status": 400, "errors": validationRes[1]}

    # print(users_data)

    return jsonify(response)


@app.route("/user", methods=['PUT'])
def updateUser():

    validationRes = updateUserFields(request.json)
    response = {}

    if validationRes[0] == 'Modificado':
        response = {"msg": "Modificado correctamente", "status": 200}
    else:
        response = {"msg": "Error al modificar ",
                    "status": 400, "errors": validationRes[1]}

    # print(users_data)

    return jsonify(response)


@app.route("/user/<user_id>", methods=['GET'])
def getUser(user_id):
    response = {}

    validationRes = searchUser(user_id)
    if validationRes[0]:
        response = validationRes[0]
    else:
        response = {"msg": "Informacion no encontrada", "status": 400}
    return jsonify(response)


@app.route("/user", methods=['GET'])
def getAllUsers():
    return jsonify({'results': users_data})
