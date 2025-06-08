"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Agregar miembros iniciales (además de John)
jackson_family.add_member({
    "first_name": "Jane",
    "age": 35,
    "lucky_numbers": [10, 14, 3]
})

jackson_family.add_member({
    "first_name": "Jimmy",
    "age": 5,
    "lucky_numbers": [1]
})

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    # Lista de todos los miembros
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# GET /members/<int:member_id> - Devuelve un solo miembro
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Miembro no encontrado"}), 400


# POST /members - Añade un nuevo miembro
@app.route('/members', methods=['POST'])
def add_member():
    try:
        data = request.get_json()
        jackson_family.add_member(data)
        return jsonify({"message": "Miembro agregado con exito"}), 200
    except:
        return jsonify({"error": "Dato invalido"}), 400


# DELETE /members/<int:member_id> - Elimina un miembro
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        jackson_family.delete_member(member_id)
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Miembro no encontrado"}), 400
    
    # NOTA: https://fictional-enigma-r4g9wj5jw4q4h5j47-3000.app.github.dev/members/5 eliminado en postman

# Esto solo se ejecuta si se ejecuta `$ python src/app.py`
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
