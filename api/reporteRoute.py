from flask import request, jsonify
from api import app
from api.borrowUtils import getReportByUserId


@app.route("/report", methods=['GET'])
def getReport():

    args = request.args.to_dict()
    response = {}

    userId = None
    returned = None

    try:
        userId = args["id_user"]
    except KeyError:
        pass

    try:
        strReturned = args["returned"].lower()

        if strReturned == 'true':
            returned = True
        elif strReturned == 'false':
            returned = False
    except KeyError:
        pass

    print(' returned recibido ', returned, ' tipo ', )

    validationRes = getReportByUserId(userId, returned)

    if validationRes[0]:
        response = {"msg": "Reporte Generado correctamente",
                    "status": 200, "data": validationRes[0]}
    else:
        response = {"msg": "Error", "status": 400, "errors": validationRes[1]}

    return jsonify(response)
