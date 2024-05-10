import json

def cargar_reportes():
    try:
        with open("reportes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_reportes(reportes):
    with open("reportes.json", "w") as file:
        json.dump(reportes, file, indent=4)

def agregar_reporte(nuevo_reporte):
    reportes = cargar_reportes()
    reportes.append(nuevo_reporte)
    guardar_reportes(reportes)

def obtener_reporte_por_id(identificador_reporte):
    reportes = cargar_reportes()
    for reporte in reportes:
        if reporte["Identificador"] == identificador_reporte:
            return reporte
    return None

def eliminar_reporte(identificador_reporte):
    reportes = cargar_reportes()
    reportes_actualizados = [reporte for reporte in reportes if reporte["Identificador"] != identificador_reporte]
    if len(reportes_actualizados) != len(reportes):
        guardar_reportes(reportes_actualizados)
        return True
    return False
