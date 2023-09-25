# PyVTInspeKtor/funcion/def_dominio.py
import requests
import argparse
import sys
import os
import time
from funcion import key

# Obtener el directorio actual del script
script_directory = os.path.dirname(os.path.abspath(__file__))
# Ruta del archivo de salida relativa al directorio del script
archivo_salida = os.path.join(script_directory, '..', 'reporte', 'dominio.txt')

# Función para escanear un solo dominio
def escanear_dominio(dominio):
    headers = {
        'x-apikey': key.VT_API_KEY  # Utilizar la clave de API desde key.py
    }

    cantidad_maliciosa = 0  # Definir la variable cantidad_maliciosa con un valor predeterminado

    try:
        respuesta = requests.get(
            f"https://www.virustotal.com/api/v3/domains/{dominio}", headers=headers)

        if respuesta.status_code == 200:
            informacion_dominio = respuesta.json()
            cantidad_maliciosa = informacion_dominio['data']['attributes']['last_analysis_stats']['malicious']
            with open(archivo_salida, 'a') as f:
                if cantidad_maliciosa > 0:
                    if cantidad_maliciosa == 1:
                        f.write(f"{dominio} - Malicioso ({cantidad_maliciosa} Motor)\n")
                    else:
                        f.write(f"{dominio} - Malicioso ({cantidad_maliciosa} Motores)\n")
                else:
                    f.write(f"{dominio} - No Malicioso\n")
        else:
            with open(archivo_salida, 'a') as f:
                f.write(f"Error al escanear {dominio}. Código de respuesta HTTP: {respuesta.status_code}\n")

    except Exception as e:
        with open(archivo_salida, 'a') as f:
            f.write(f"Error al escanear {dominio}: {str(e)}\n")

    return cantidad_maliciosa
# PyVTInspeKtor/funcion/def_dominio.py
