from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Definición del modelo Usuario
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(255), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)

# Conexión a PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    database="crud",
    user="postgres",
    password="postgres"
)


# Ruta para obtener todos los usuarios
@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.order_by(Usuario.id.asc()).all()  # Ordena los usuarios por ID ascendente
    usuarios_list = [
        {"id": u.id, "correo": u.correo, "nombre": u.nombre, "edad": u.edad} for u in usuarios
    ]
    
    # Imprimir los usuarios en la consola para verificar
    print(usuarios_list)

    return jsonify(usuarios_list)


# Ruta para obtener un usuario en específico
@app.route('/api/usuarios/<int:id>', methods=['GET'])
def obtener_usuario_por_id(id):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s;", (id,))
    usuario = cursor.fetchone()
    cursor.close()

    if usuario:
        return jsonify({"id": usuario[0], "correo": usuario[1], "nombre": usuario[2], "edad": usuario[3]})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404


# Crear un nuevo usuario
@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud
    correo = data.get('correo')
    nombre = data.get('nombre')
    edad = data.get('edad')
    id = data.get('id')  # Obtener el ID si se proporciona

    # Verificar que todos los campos necesarios están presentes
    if not correo or not nombre or not edad:
        return jsonify({"mensaje": "Faltan datos"}), 400

    # Insertar usuario con ID especificado o dejar que la secuencia asigne uno
    if id:
        nuevo_usuario = Usuario(id=id, correo=correo, nombre=nombre, edad=edad)
    else:
        nuevo_usuario = Usuario(correo=correo, nombre=nombre, edad=edad)

    db.session.add(nuevo_usuario)
    db.session.commit()  # Confirmar los cambios en la base de datos

    return jsonify({"id": nuevo_usuario.id, "correo": nuevo_usuario.correo, "nombre": nuevo_usuario.nombre, "edad": nuevo_usuario.edad}), 201



# Actualizar un usuario existente
@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud
    correo = data.get('correo')
    nombre = data.get('nombre')
    edad = data.get('edad')

    # Verificar que al menos uno de los campos está presente
    if not (correo or nombre or edad):
        return jsonify({"mensaje": "Faltan datos para actualizar"}), 400

    cursor = conexion.cursor()

    # Construir la consulta de actualización
    updates = []
    params = []
    
    if correo:
        updates.append("correo = %s")
        params.append(correo)
    if nombre:
        updates.append("nombre = %s")
        params.append(nombre)
    if edad:
        updates.append("edad = %s")
        params.append(edad)

    params.append(id)  # Agregar el ID al final para la consulta

    query = f"UPDATE usuarios SET {', '.join(updates)} WHERE id = %s;"
    cursor.execute(query, params)
    conexion.commit()  # Confirmar los cambios en la base de datos
    cursor.close()

    return jsonify({"mensaje": "Usuario actualizado con éxito"}), 200


# Ruta para eliminar un usuario
@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    # Conectar a la base de datos
    conexion = psycopg2.connect(
        host="localhost",
        database="crud",
        user="postgres",
        password="postgres"
    )
    cursor = conexion.cursor()

    # Ejecutar la consulta para eliminar el usuario
    cursor.execute("DELETE FROM usuarios WHERE id = %s;", (id,))
    conexion.commit()  # Confirmar los cambios en la base de datos
    cursor.close()

    if cursor.rowcount == 0:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    return jsonify({"mensaje": "Usuario eliminado exitosamente"}), 200


# Ruta para obtener el total de usuarios
@app.route('/api/usuarios/total', methods=['GET'])
def obtener_total_usuarios():
    total = Usuario.query.count()  # Contar el número total de usuarios
    return jsonify({"total_usuarios": total}), 200


if __name__ == '__main__':
    app.run(debug=True)