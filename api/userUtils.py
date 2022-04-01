
from operator import pos
from re import A
from api import users_data

def validateUserData(requestJSON):

    errors = []
    data = {}

    try:
        posibleId= requestJSON["id_user"]

        if userIdExist(posibleId):
            errors.append('Id ya registrada')
        else:
            data["id_user"] = posibleId
            
    except KeyError:
        errors.append('El ID de usuario es requerida')
    try:
        data["user_name"] = requestJSON["user_name"]
    except KeyError:
        errors.append('El nombre de usuario es requerido')
    try:
        data["user_nickname"] = requestJSON["user_nickname"]
    except KeyError:
        errors.append('El nickname es requerido')
    try:
        data["user_password"] = requestJSON["user_password"]
    except KeyError:
        errors.append('La contraseña es requerida')
    try:
        posibleRol = requestJSON["user_rol"].lower()
        if isValidRole(posibleRol):
            data["user_rol"] = posibleRol
        else:
            errors.append('No es un rol valido')
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
                updateData["user_name"] = requestJSON["user_name"]
            except KeyError:
                pass
            try:
                updateData["user_nickname"] = requestJSON["user_nickname"]
            except KeyError:
                pass
            try:
                updateData["user_password"] = requestJSON["user_password"]
            except KeyError:
                pass
            try:
                posibleRol = requestJSON["user_rol"].lower()
                if isValidRole(posibleRol):
                    updateData["user_rol"] = posibleRol
                else:
                    errors.append('No es un rol valido')
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

    return ['',errors]


def searchUser(idToSearch):
    
    errors = []
    
    if userIdExist(idToSearch):
        for user in users_data:
            if user['id_user'] == idToSearch:
                return [user, None]
    else:
        errors.append('Id no registrada')

    return [None,errors]


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