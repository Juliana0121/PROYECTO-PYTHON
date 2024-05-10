import json
def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def guardar_datos(datos, archivo):
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=4)

def crear_servicio(categoria, nombre, detalles, precio, archivo):
    datos = cargar_datos(archivo) or {"Servicios": {}}
    datos["Servicios"].setdefault(categoria, {})
    datos["Servicios"][categoria][nombre] = {"detalles": detalles, "precio": precio}
    guardar_datos(datos, archivo)

def leer_servicios(archivo):
    datos = cargar_datos(archivo)
    return datos["Servicios"] if datos and "Servicios" in datos else {}

def actualizar_servicio(categoria, nombre, nuevos_detalles, nuevo_precio, archivo):
    datos = cargar_datos(archivo)
    if datos and categoria in datos["Servicios"] and nombre in datos["Servicios"][categoria]:
        datos["Servicios"][categoria][nombre]["detalles"] = nuevos_detalles
        datos["Servicios"][categoria][nombre]["precio"] = nuevo_precio
        guardar_datos(datos, archivo)
        return True
    return False

def eliminar_servicio(categoria, nombre, archivo):
    datos = cargar_datos(archivo)
    if datos and categoria in datos["Servicios"] and nombre in datos["Servicios"][categoria]:
        del datos["Servicios"][categoria][nombre]
        guardar_datos(datos, archivo)
        return True
    return False


def crear_producto(nombre, precio, caracteristicas, archivo):
    datos = cargar_datos(archivo) or {"Productos": {}}
    datos["Productos"][nombre] = {"precio": precio, "caracteristicas": caracteristicas}
    guardar_datos(datos, archivo)

def leer_productos(archivo):
    datos = cargar_datos(archivo)
    return datos["Productos"] if datos and "Productos" in datos else {}

def actualizar_producto(nombre, nuevo_precio, nuevas_caracteristicas, archivo):
    datos = cargar_datos(archivo)
    if datos and nombre in datos["Productos"]:
        datos["Productos"][nombre]["precio"] = nuevo_precio
        datos["Productos"][nombre]["caracteristicas"] = nuevas_caracteristicas
        guardar_datos(datos, archivo)
        return True
    return False

def eliminar_producto(nombre, archivo):
    datos = cargar_datos(archivo)
    if datos and nombre in datos["Productos"]:
        del datos["Productos"][nombre]
        guardar_datos(datos, archivo)
        return True
    return False

archivo = "datos.json"


"""
crear_servicio("Internet", "Internet Hogar 100MB/s", "Velocidad alta de internet", "150000 COP", archivo)

print("Servicios:")
print(leer_servicios(archivo))

actualizar_servicio("Internet", "Internet Hogar 100MB/s", "Velocidad ultra alta de internet", "200000 COP", archivo)

eliminar_servicio("Internet", "Internet Hogar 100MB/s", archivo)

print("Servicios después de eliminar uno:")
print(leer_servicios(archivo))

crear_producto("Xiaomi Redmi Note 10s", "537719 COP", {"Memoria interna": "128 GB", "Cámara frontal principal": "13 Mpx", "Cámara trasera principal": "64 Mpx"}, archivo)

print("Productos:")
print(leer_productos(archivo))

actualizar_producto("Xiaomi Redmi Note 10s", "550000 COP", {"Memoria interna": "128 GB", "Cámara frontal principal": "16 Mpx", "Cámara trasera principal": "64 Mpx"}, archivo)

eliminar_producto("Xiaomi Redmi Note 10s", archivo)

print("Productos después de eliminar uno:")
print(leer_productos(archivo))
"""