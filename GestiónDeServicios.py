import json

def cargar_servicios():
    try:
        with open("servicios.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_servicios(servicios):
    with open("servicios.json", "w") as file:
        json.dump(servicios, file, indent=4)

def agregar_servicio(nuevo_servicio):
    servicios = cargar_servicios()
    servicios.append(nuevo_servicio)
    guardar_servicios(servicios)

def obtener_servicio_por_identificador(identificador_servicio):
    servicios = cargar_servicios()
    for servicio in servicios:
        if servicio["Identificador"] == identificador_servicio:
            return servicio
    return None

def actualizar_servicio(identificador_servicio, datos_actualizados):
    servicios = cargar_servicios()
    for servicio in servicios:
        if servicio["Identificador"] == identificador_servicio:
            servicio.update(datos_actualizados)
            guardar_servicios(servicios)
            return True
    return False

def eliminar_servicio(identificador_servicio):
    servicios = cargar_servicios()
    for servicio in servicios:
        if servicio["Identificador"] == identificador_servicio:
            servicios.remove(servicio)
            guardar_servicios(servicios)
            return True
    return False 