import json

def cargar_productos():
    try:
        with open('productos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_productos(productos):
    with open('productos.json', 'w') as file:
        json.dump(productos, file, indent=4)

def agregar_producto(nuevo_producto):
    productos = cargar_productos()
    productos.append(nuevo_producto)
    guardar_productos(productos)

def obtener_producto_por_id(id_producto):
    productos = cargar_productos()
    for producto in productos:
        if producto['id'] == id_producto:
            return producto
    return None

def actualizar_producto(id_producto, datos_actualizados):
    productos = cargar_productos()
    for producto in productos:
        if producto['id'] == id_producto:
            producto.update(datos_actualizados)
            guardar_productos(productos)
            return True
    return False

def eliminar_producto(id_producto):
    productos = cargar_productos()
    for producto in productos:
        if producto['id'] == id_producto:
            productos.remove(producto)
            guardar_productos(productos)
            return True
    return False