import json

def cargar_usuarios():
    try:
        with open('usuarios.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file, indent=4)

def agregar_usuario(nuevo_usuario):
    usuarios = cargar_usuarios()
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)

def obtener_usuario_por_identificador(identificador_usuario):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["Identificador"] == identificador_usuario:
            return usuario
    return None

def actualizar_usuario(identificador_usuario, datos_actualizados):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["Identificador"] == identificador_usuario:
            usuario.update(datos_actualizados)
            guardar_usuarios(usuarios)
            return True
    return False

def eliminar_usuario(identificador_usuario):
    usuarios = cargar_usuarios()
    usuarios_actualizados = [usuario for usuario in usuarios if usuario["Identificador"] != identificador_usuario]
    if len(usuarios_actualizados) != len(usuarios):
        guardar_usuarios(usuarios_actualizados)
        return True
    return False
