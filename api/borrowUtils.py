from datetime import date
from api import borrow_data
from api.userUtils import isUserAvailable, userIdExist
from api.booksUtils import isBookAvailable, updateCopies, bookIdExist, searchBookById

borrowIdCorrelative = 1

# today = date.today()

def createNewBorrow(borrowInfo):
    errors = []
    data = {}

    try:
        userId = borrowInfo["id_user"]

        if userIdExist(userId):
            try:
                bookId = borrowInfo["id_book"]
                if bookIdExist(bookId):
                    if isUserAvailable(userId):
                        
                        if isBookAvailable(bookId):
                            updateCopies(bookId, False)

                            book = searchBookById(bookId) 
                            global borrowIdCorrelative
                            correlativo = borrowIdCorrelative

                            dateStr = date.today().strftime("%d/%m/%Y")

                            data = {"id_borrow":correlativo, "date": dateStr, "returned": False, "id_user": userId, "book":book}
                            borrowIdCorrelative+=1

                            return [data, None]
                        else:
                            errors.append('No existe disponibilidad')
                    else:
                        errors.append('Usuario no apto para prestamos')
                else:
                    errors.append('Id de libro no registrada')

            except KeyError:
                errors.append('El atributo id_book es requerido')
        else:
            errors.append('Id de usuario no registrada')
    except KeyError:
        errors.append('El atributo id_user es requerido')

    return [None, errors]

