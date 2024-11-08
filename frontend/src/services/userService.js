const API_URL = "http://localhost:5000/api/usuarios";


// Obtener todos los usuarios
export const obtenerUsuarios = async () => {
    const response = await fetch(API_URL);
    return response.json();
};


// Obtener un usuario específico por ID
export const obtenerUsuarioPorId = async (id) => {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
};


// Crear un nuevo usuario
export const agregarUsuario = async (usuario) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(usuario)
    });

    const data = await response.json();
    console.log(data); // Para verificar la respuesta
    return data;
};


// Actualizar un usuario existente
export const actualizarUsuario = async (id, datosActualizados) => {
    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datosActualizados)
    });
    return response.json();
};


// Eliminar un usuario
export const eliminarUsuario = async (id) => {
    const response = await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    });
    return response.json();
};


// Obtener el total de usuarios
export const obtenerTotalUsuarios = async () => {
    const response = await fetch(`${API_URL}/total`);
    return response.json();
};