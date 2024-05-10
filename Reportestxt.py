"""
import datetime

with open("reportes.txt","a") as reporte:
        fechaHora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        reporte.write("\n" + fechaHora + " - " + mensaje)

"""
        