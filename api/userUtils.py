
from operator import pos
from re import A
from api import users_data


def validateUserData(requestJSON):

    errors = []
    data = {}

    try:
        posibleId = requestJSON["id_user"]
        if len(posibleId) > 0:
            if userIdExist(posibleId):
                errors.append('Id ya registrada')
            else:
                data["id_user"] = posibleId
        else:
            errors.append('El ID de usuario no puede estar vacia')

    except KeyError:
        errors.append('El ID de usuario es requerida')
    try:
        if len(requestJSON["user_name"]) > 0:
            data["user_name"] = requestJSON["user_name"]
        else:
            errors.append('El username de usuario no puede estar vacio')
    except KeyError:
        errors.append('El nombre de usuario es requerido')
    try:
        if len(requestJSON["user_nickname"]) > 0:
            data["user_nickname"] = requestJSON["user_nickname"]
        else:
            errors.append('El nickname de usuario no puede estar vacio')
    except KeyError:
        errors.append('El nickname es requerido')
    try:
        if len(requestJSON["user_password"]) > 0:
            data["user_password"] = requestJSON["user_password"]
        else:
            errors.append('La contraseña no puede estar vacia')
    except KeyError:
        errors.append('La contraseña es requerida')
    try:
        posibleRol = requestJSON["user_rol"].lower()
        if len(posibleRol) > 0:
            if isValidRole(posibleRol):
                data["user_rol"] = posibleRol
            else:
                errors.append('No es un rol valido')
        else:
            errors.append('El rol no puede estar vacio')

    except KeyError:
        errors.append('El rol es requerido')
    try:
        posibleAvailable = requestJSON["available"]
        if isValidAvailable(posibleAvailable):
            data["available"] = posibleAvailable
        else:
            errors.append('El estado debe ser booleano')
    except KeyError:
        errors.append('El estado es requerido')

    if len(errors) > 0:
        return [None, errors]
    else:
        return [data, None]


def updateUserFields(requestJSON):

    errors = []

    try:
        idToUpdate = requestJSON["id_user"]

        if userIdExist(idToUpdate):

            updateData = {}

            try:
                if len(requestJSON["user_name"]) > 0:
                    updateData["user_name"] = requestJSON["user_name"]
                else:
                    errors.append('el user name no puede estar vacio')
            except KeyError:
                pass
            try:
                if len(requestJSON["user_nickname"]) > 0:
                    updateData["user_nickname"] = requestJSON["user_nickname"]
                else:
                    errors.append('el user nickname no puede estar vacio')
            except KeyError:
                pass
            try:
                if len(requestJSON["user_password"]) > 0:
                    updateData["user_password"] = requestJSON["user_password"]
                else:
                    errors.append('el user password no puede estar vacio')

            except KeyError:
                pass
            try:
                if len(requestJSON["user_rol"]) > 0:
                    posibleRol = requestJSON["user_rol"].lower()
                    if isValidRole(posibleRol):
                        updateData["user_rol"] = posibleRol
                    else:
                        errors.append('No es un rol valido')
                else:
                    errors.append('el user role no puede estar vacio')

            except KeyError:
                pass
            try:
                posibleAvailable = requestJSON["available"]

                if isValidAvailable(posibleAvailable):
                    updateData["available"] = posibleAvailable
                else:
                    errors.append('El estado debe ser booleano')

            except KeyError:
                pass

            for user in users_data:
                if user['id_user'] == idToUpdate:
                    user.update(updateData)
                    return ['Modificado', errors]

        else:
            errors.append('Id no registrada')
    except KeyError:
        errors.append('El ID de usuario es requerida')

    return ['', errors]


def searchUser(idToSearch):

    errors = []

    if userIdExist(idToSearch):
        for user in users_data:
            if user['id_user'] == idToSearch:
                return [user, None]
    else:
        errors.append('Id no registrada')

    return [None, errors]


def isUserAvailable(idToSearch):
    if userIdExist(idToSearch):
        for user in users_data:
            if user['id_user'] == idToSearch:
                return user["available"]


def userIdExist(id):
    posiblesIds = []
    for user in users_data:
        try:
            posiblesIds.append(user['id_user'])
        except:
            pass

    return (id in posiblesIds)


def isValidRole(role):
    posibleRoles = ['estudiante', 'catedratico']
    return role in posibleRoles


def isValidAvailable(available):
    posibleAvailables = [True, False]
    return available in posibleAvailables
