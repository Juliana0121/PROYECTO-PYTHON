def menu_principal():
    print("----------------------------------------")
    print("Bienvenido a Claro")
    print("----------------------------------------")
    print("Opciones")
    print("1. Administración de usuarios ")
    print("2. Administración de servicios ")
    print("4. Ventas ")
    print("5. Reportes")
    print("6. Salir")
    print("----------------------------------------")
    
def menu_administración_usuarios():
    print("----------------------------------------")
    print("Opción: Administración de usuarios")
    print("1. Registro y administraión de usuarios ")
    print("2. Historial de usuarios ")
    print("3. Personalizacion de servicios ")
    print("4. Administración de ventas")
    print("5. Salir al menú principal")
    print("----------------------------------------")    
    
def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("----------------------------------------")
        return opc
    except Exception:
        print("Valor inválido")
        print("----------------------------------------")
        return -1