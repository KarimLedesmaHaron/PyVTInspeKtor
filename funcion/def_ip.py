# PyVTInspeKtor/funcion/def_ip.py
import requests
import argparse
import sys
from funcion import key
import os
import time

# Obtener el directorio actual del script
script_directory = os.path.dirname(os.path.abspath(__file__))
# Ruta del archivo de salida relativa al directorio del script
archivo_salida = os.path.join(script_directory, '..', 'reporte', 'ip.txt')

# Función para escanear una sola IP
def escanear_ip(ip):
    headers = {
        'x-apikey': key.VT_API_KEY  # Utilizar la clave de API desde key.py
    }

    respuesta = requests.get(
        f"https://www.virustotal.com/api/v3/ip_addresses/{ip}", headers=headers)

    informacion_ip = respuesta.json()

    try:
        cantidad_maliciosa = informacion_ip['data']['attributes']['last_analysis_stats']['malicious']

        with open(archivo_salida, 'a') as archivo:
            if cantidad_maliciosa > 0:
                if cantidad_maliciosa == 1:
                    mensaje = f"{ip} - Malicioso ({cantidad_maliciosa} Motor)\n"
                else:
                    mensaje = f"{ip} - Malicioso ({cantidad_maliciosa} Motores)\n"
                archivo.write(mensaje)
                print(mensaje)
            else:
                mensaje = f"{ip} - No Malicioso\n"
                archivo.write(mensaje)
                print(mensaje)

        return cantidad_maliciosa
    except:
        print(respuesta.text)
        return 0
# PyVTInspeKtor/funcion/def_ip.py
