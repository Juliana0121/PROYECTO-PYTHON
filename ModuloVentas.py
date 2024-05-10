import json
from datetime import datetime

def cargar_ventas(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"Productos_Vendidos": [], "Servicios_Vendidos": []}

def guardar_ventas(ventas, archivo):
    with open(archivo, 'w') as file:
        json.dump(ventas, file, indent=4)

def agregar_venta(tipo, nombre, cantidad, precio, fecha, archivo):
    ventas = cargar_ventas(archivo)
    venta = {
        "Tipo": tipo,
        "Nombre": nombre,
        "Cantidad": cantidad,
        "Precio": precio,
        "Fecha": fecha.strftime("%Y-%m-%d %H:%M:%S")
    }
    if tipo == "Producto":
        ventas["Productos_Vendidos"].append(venta)
    elif tipo == "Servicio":
        ventas["Servicios_Vendidos"].append(venta)
    guardar_ventas(ventas, archivo)

