from datos import *
import Ventas,os
import Menu_Administrador


while True:
    Menu_Administrador.menu_principal()
    option = Menu_Administrador.pedir_opcion()
    if option == 1:
        os.system("clear")
        Menu_Administrador.menu_administración_usuarios()

guardar_datos(datos, RUTA_SERVICIO)