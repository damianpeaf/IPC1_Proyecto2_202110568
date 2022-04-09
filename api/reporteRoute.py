from flask import request, jsonify
from api import app
from api.booksUtils import bookReport
from api.borrowUtils import getReportByUserId


@app.route("/report", methods=['GET'])
def getReport():
    response = bookReport()
    return jsonify(response)
