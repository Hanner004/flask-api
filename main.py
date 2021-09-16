from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = []

#crear usuarios
@app.route("/users", methods=["POST"])
def create():
    body = json.loads(request.data)
    id = body["id"]
    name = body["name"]
    lastname = body["lastname"]
    newUser = {
        "id": id,
        "name": name,
        "lastname": lastname
    }
    users.append(newUser)
    return  jsonify(newUser), 200
    
#consultar usuarios
@app.route("/users", methods=["GET"])
def findAll():
    return jsonify(users), 200

#consultar usuario
@app.route("/users/<int:id>", methods=["GET"])
def findOne(id):
    result = next((user for user in users if user["id"] == id), None)
    if result is not None:
        return jsonify(result), 200
    else:
        return "USER NOT FOUND", 404

#actualizar usuario
@app.route("/users/<int:id>", methods=["PUT"])
def update(id):
    body = json.loads(request.data)
    newId = body["id"]
    newName = body["name"]
    newLastname = body["lastname"]
    updateUser = {
        "id": newId,
        "name": newName,
        "lastname": newLastname
    }
    userUpdated = None
    for index, user in enumerate(users):
        if user["id"] == id:
            userUpdated = updateUser
            user[index] = updateUser
    if userUpdated is not None:
        return "USER UPDATED", 200
    else:
        return "USER NOT FOUND", 404
    

#eliminar usuario
@app.route("/users/<int:id>", methods=["DELETE"])
def delete(id):
    userFound = None
    for index, user in enumerate(users):
        if user["id"]== id:
            userFound = user
            users.pop(index)
    if userFound is not None:
        return "USER DELETED", 200
    else:
        return "USER NOT FOUND", 404

if __name__ == "__main__":
    app.run(debug=True)
