CREATE TABLE IF NOT EXISTS tasks( -- crea la tabla tasks si no existe 
-- Esta tabla es para manejar las tareas del usuario
    id INTEGER PRIMARY KEY, --llave primaria 
    title TEXT NO NULL, --texto
    created_date TEXT NO NULL, -- la fecha de creacion
    completed INTEGER NOT NULL DEFAULT 0 -- si la tarea esta completa un 1 sino un 0

)