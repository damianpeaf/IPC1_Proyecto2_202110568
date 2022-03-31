from re import A
from urllib import response
from flask import request
from api import app
from api import books_data
from api.booksUtils import createBook, updateBookFields, deleteBookById, serchBookByAuthorOrTitle

# Id: identificador alfanumérico (letras y números).
# Author: nombre del autor del libro.
# Títle: título del libro.
# Edition: número de edición del libro.
# Editorial: editorial del libro.
# Year: año de publicación.
# Description: breve descripción del libro.
# Available copies: copias disponibles para prestar.
# copies: copias no disponibles para prestar.
# Copies: total de copias existentes.

@app.route("/book", methods=['POST'])
def createBooks():

    response = {}

    booksArr = request.json
    messagePerBook = []

    for book in booksArr:
        validationRes = createBook(book)

        if validationRes[0]:
            books_data.append(validationRes[0])

        messagePerBook.append(validationRes[1])        

    response= {"msg": messagePerBook,"status": 200}

    return response

@app.route("/book", methods=['PUT'])
def updateBook():

    validationRes = updateBookFields(request.json)
    response={}

    if validationRes[0] == 'Modificado':
        response= {"msg": "Modificado correctamente","status": 200}
    else:
        response= {"msg": "Error al modificar ","status": 400, "errors": validationRes[1]}

    print(books_data)

    return response

@app.route("/book/<book_id>", methods=['DELETE'])
def deleteBook(book_id):
    response = {}

    validationRes = deleteBookById(book_id)
    if validationRes[0]:
        response= validationRes[0]
    else:
        response= {"msg": "Registro eliminado ","status": 200}
    return response

@app.route("/book", methods=['GET'])
def searchBook():

    args = request.args.to_dict()

    searchResp = serchBookByAuthorOrTitle(args)

    response = {"results found":searchResp}

    return response