from enum import auto
from api import books_data


def createBook(books):
    errors = []
    data = {}

    try:
        posibleId = books["id_book"]

        if bookIdExist(posibleId):
            errors.append('Id ya registrada')
        else:
            data["id_book"] = posibleId

    except KeyError:
        errors.append('El ID del libro es requerida')

    keys = ["book_author", "book_title", "book_edition", "book_editorial", "book_year",
            "book_description", "book_available_copies", "book_unavailable_copies", "book_copies"]

    for key in keys:
        try:
            data[key] = books[key]
        except KeyError:
            errors.append('El atributo ' + key+' es requerido')

    if len(errors) > 0:
        return [None, errors]
    else:
        return [data, ['Creado correctamente']]


def updateBookFields(book):

    errors = []

    try:
        idToUpdate = book["id_book"]

        if bookIdExist(idToUpdate):

            updateData = {}

            keys = ["book_author", "book_title", "book_edition", "book_editorial", "book_year",
                    "book_description", "book_available_copies", "book_unavailable_copies", "book_copies"]

            for key in keys:
                try:
                    updateData[key] = book[key]
                except KeyError:
                    pass

            for bok in books_data:
                if bok['id_book'] == idToUpdate:
                    bok.update(updateData)
                    return ['Modificado', errors]

        else:
            errors.append('ID no registrada')
    except KeyError:
        errors.append('El ID de usuario es requerida')

    return ['', errors]


def deleteBookById(book_id):
    errors = []

    if bookIdExist(book_id):

        for book in books_data:
            if book['id_book'] == book_id:

                index = books_data.index(book)

                del books_data[index]

                # print(books_data)

                return [False]
    else:
        errors.append('Id no registrada')

    return errors


def serchBookByAuthorOrTitle(args):

    autor = ''
    titulo = ''

    try:
        autor = args["author"]
    except KeyError:
        pass
    try:
        titulo = args["titulo"]
    except KeyError:
        pass

    dataFound = []

    # Busqueda por autor
    for book in books_data:
        if book["book_author"] == autor:
            dataFound.append(book)

    # Busqueda por titulo
    for book in books_data:
        if book["book_title"] == titulo:
            dataFound.append(book)

    return dataFound

# , updateCopies, ,


def isBookAvailable(idB):
    if bookIdExist(idB):
        for book in books_data:
            if book['id_book'] == idB:
                return (book['book_available_copies'] > 0)


def searchBookById(idB):
    if bookIdExist(idB):
        for book in books_data:
            if book['id_book'] == idB:
                return book


def updateCopies(idB, increase):
    if bookIdExist(idB):
        for book in books_data:
            if book['id_book'] == idB:
                availableCopies = book["book_available_copies"]
                unavailableCopies = book["book_unavailable_copies"]

                if increase:
                    availableCopies += 1
                    unavailableCopies -= 1
                else:
                    availableCopies -= 1
                    unavailableCopies += 1

                validationRes = updateBookFields(
                    {"id_book": idB, "book_available_copies": availableCopies, "book_unavailable_copies": unavailableCopies})
                return True

    return False


def bookIdExist(idE):
    posiblesIds = []
    for book in books_data:
        try:
            posiblesIds.append(book['id_book'])
        except:
            pass

    return (idE in posiblesIds)
