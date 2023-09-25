# PyVTInspeKtor/funcion/def_hash.py
import requests
import argparse
import sys
import os
import time
from funcion import key

# Obtener el directorio actual del script
script_directory = os.path.dirname(os.path.abspath(__file__))
# Ruta del archivo de salida relativa al directorio del script
archivo_salida = os.path.join(script_directory, '..', 'reporte', 'hash.txt')

# Función para escanear un solo hash
def escanear_hash(hash_value):
    headers = {
        'x-apikey': key.VT_API_KEY  # Utilizar la clave de API desde key.py
    }

    cantidad_maliciosa = 0  # Inicializar la variable cantidad_maliciosa con un valor predeterminado

    try:
        api_url = f"https://www.virustotal.com/api/v3/files/{hash_value}"

        respuesta = requests.get(api_url, headers=headers)

        if respuesta.status_code == 200:
            informacion_hash = respuesta.json()
            cantidad_maliciosa = informacion_hash['data']['attributes']['last_analysis_stats']['malicious']
            with open(archivo_salida, 'a') as f:
                if cantidad_maliciosa > 0:
                    if cantidad_maliciosa == 1:
                        f.write(f"{hash_value} - Malicioso ({cantidad_maliciosa} Motor)\n")
                    else:
                        f.write(f"{hash_value} - Malicioso ({cantidad_maliciosa} Motores)\n")
                else:
                    f.write(f"{hash_value} - No Malicioso\n")
        else:
            with open(archivo_salida, 'a') as f:
                f.write(f"Error al escanear {hash_value}. Código de respuesta HTTP: {respuesta.status_code}\n")

    except Exception as e:
        with open(archivo_salida, 'a') as f:
            f.write(f"Error al escanear {hash_value}: {str(e)}\n")

    return cantidad_maliciosa

