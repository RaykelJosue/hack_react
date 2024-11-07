const STORAGE_KEY = 'usuarios';

// Función auxiliar para obtener usuarios del localStorage
const getUsuariosFromStorage = () => {
  const usuarios = localStorage.getItem(STORAGE_KEY);
  return usuarios ? JSON.parse(usuarios) : [];
};

// Función auxiliar para guardar usuarios en localStorage
const saveUsuariosToStorage = (usuarios) => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(usuarios));
};

// Obtener todos los usuarios
export const obtenerUsuarios = async () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(getUsuariosFromStorage());
    }, 100);
  });
};

// Obtener un usuario específico por ID
export const obtenerUsuarioPorId = async (id) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const usuarios = getUsuariosFromStorage();
      const usuario = usuarios.find(u => u.id === id);
      if (usuario) {
        resolve(usuario);
      } else {
        reject(new Error('Usuario no encontrado'));
      }
    }, 100);
  });
};

// Crear un nuevo usuario
export const agregarUsuario = async (usuario) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      const usuarios = getUsuariosFromStorage();
      const nuevoUsuario = {
        ...usuario,
        id: Date.now().toString() // Generamos un ID único
      };
      usuarios.push(nuevoUsuario);
      saveUsuariosToStorage(usuarios);
      resolve(nuevoUsuario);
    }, 100);
  });
};

// Actualizar un usuario existente
export const actualizarUsuario = async (id, datosActualizados) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const usuarios = getUsuariosFromStorage();
      const index = usuarios.findIndex(u => u.id === id);
      if (index !== -1) {
        usuarios[index] = { ...usuarios[index], ...datosActualizados };
        saveUsuariosToStorage(usuarios);
        resolve(usuarios[index]);
      } else {
        reject(new Error('Usuario no encontrado'));
      }
    }, 100);
  });
};

// Eliminar un usuario
export const eliminarUsuario = async (id) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      const usuarios = getUsuariosFromStorage();
      const nuevosUsuarios = usuarios.filter(u => u.id !== id);
      saveUsuariosToStorage(nuevosUsuarios);
      resolve({ success: true });
    }, 100);
  });
};

// Obtener el total de usuarios
export const obtenerTotalUsuarios = async () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      const usuarios = getUsuariosFromStorage();
      resolve(usuarios.length);
    }, 100);
  });
};