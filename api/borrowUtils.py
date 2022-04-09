from datetime import date
from api import borrow_data
from api.userUtils import isUserAvailable, userIdExist
from api.booksUtils import isBookAvailable, updateCopies, bookIdExist, searchBookById

borrowIdCorrelative = 1


def returnBook(borrow_id):
    errors = []

    borrow_id = int(borrow_id)

    print('ID recibida ', borrow_id)

    if borrowIdExist(borrow_id):
        if not isBorrowReturned(borrow_id):

            borrowToModify = searchBorrowById(borrow_id)
            bookBorrow = borrowToModify['borrow_book']
            bookIdBorrow = bookBorrow['id_book']

            updateCopies(bookIdBorrow, True)

            for borrow in borrow_data:
                if borrow['id_borrow'] == borrow_id:

                    updateData = {"returned": True}
                    borrow.update(updateData)
                    return [True, errors]

        else:
            errors.append('El prestamo ya ha sido devuelto')
    else:
        errors.append('No existe la ID del prestamo')

    return [False, errors]


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

                            data = {"id_borrow": correlativo, "borrow_date": dateStr,
                                    "returned": False, "id_user": userId, "borrow_book": book}
                            borrowIdCorrelative += 1

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


def searchBorrow(idB):
    errors = []

    if borrowIdExist(idB):
        borrow = searchBorrowById(idB)
        return [borrow, None]
    else:
        errors.append('Id del prestamo no encontrada')

    return [None, errors]


def borrowIdExist(idB):
    posiblesIds = []

    print(borrow_data)

    for borrow in borrow_data:
        try:
            posiblesIds.append(borrow['id_borrow'])
        except:
            pass

    print('comparando ', idB, ' con ', posiblesIds, (idB in posiblesIds))

    return (idB in posiblesIds)


def getReportByUserId(idU, returned):

    errors = []
    data = []

    if idU is not None:
        if(userIdExist(idU)):

            for borrow in borrow_data:

                clause = True
                if returned == True:
                    clause = (borrow['id_user'] ==
                              idU and borrow['returned'] == True)
                elif returned == False:
                    clause = (borrow['id_user'] ==
                              idU and borrow['returned'] == False)
                else:
                    clause = (borrow['id_user'] == idU)

                if clause:
                    data.append(borrow)

            return [data, False]

        else:
            errors.append('No existe usuario con dicha ID')
    else:
        errors.append('El id de usuario es requerida')

    return [False, errors]


def isBorrowReturned(idB):
    for borrow in borrow_data:
        if borrow['id_borrow'] == idB:
            return borrow['returned']


def searchBorrowById(idB):
    for borrow in borrow_data:
        if borrow['id_borrow'] == idB:
            return borrow
