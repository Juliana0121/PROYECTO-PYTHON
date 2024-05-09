import json

def cargar_ventas():
    try:
        with open('ventas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_ventas(ventas):
    with open('ventas.json', 'w') as file:
        json.dump(ventas, file, indent=4)

def agregar_venta(nueva_venta):
    ventas = cargar_ventas()
    ventas.append(nueva_venta)
    guardar_ventas(ventas)

def obtener_venta_por_identificador(identificador_venta):
    ventas = cargar_ventas()
    for venta in ventas:
        if venta["identificador_venta"] == identificador_venta:
            return venta
    return None

def eliminar_venta(identificador_venta):
    ventas = cargar_ventas()
    ventas_actualizadas = [venta for venta in ventas if venta['id_venta'] != identificador_venta]
    if len(ventas_actualizadas) != len(ventas):
        guardar_ventas(ventas_actualizadas)
        return True
    return False
