from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simulación de datos en memoria
usuarios = [
    {"id": 1, "correo": "raykelquevedo@gmail.com", "nombre": "Raykel Quevedo", "edad": 21},
    {"id": 2, "correo": "johnwick@hotmail.com", "nombre": "John Wick", "edad": 52},
    {"id": 3, "correo": "tonystark@starkindustries.com", "nombre": "Tony Stark", "edad": 45}
]

# Ruta para obtener todos los usuarios
@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

# Ruta para obtener un usuario en específico
@app.route('/api/usuarios/<int:id>', methods=['GET'])
def obtener_usuario_por_id(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

# Crear un nuevo usuario
@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nuevo_usuario = {
        "id": max(u["id"] for u in usuarios) + 1,
        "correo": data.get('correo'),
        "nombre": data.get('nombre'),
        "edad": data.get('edad')
    }
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

# Actualizar un usuario existente
@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.get_json()
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        usuario.update({k: v for k, v in data.items() if v is not None})
        return jsonify({"mensaje": "Usuario actualizado con éxito"}), 200
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

# Ruta para eliminar un usuario
@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    global usuarios
    usuarios = [u for u in usuarios if u["id"] != id]
    return jsonify({"mensaje": "Usuario eliminado exitosamente"}), 200

# Ruta para obtener el total de usuarios
@app.route('/api/usuarios/total', methods=['GET'])
def obtener_total_usuarios():
    total = len(usuarios)
    return jsonify({"total_usuarios": total}), 200

if __name__ == '__main__':
    app.run(debug=True)
