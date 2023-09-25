# PyVTInspeKtor/PyVTInspeKtor.py
"""
PyVTInspeKtor - Herramienta de Escaneo de Dominios e IPs

Autor: "K" kharon.it@gmail.com
Fecha: 24 de Septiembre 2023
Ubicación: Córdoba, Argentina

Instrucciones de uso:
1. Asegúrate de que las dependencias estén instaladas utilizando `pip install -r requirements.txt`.
2. Prepara tus listas de dominios en 'objetivo/dominio.txt' y de IPs en 'objetivo/ip.txt'.
3. Ejecuta este script para escanear y analizar los dominios e IPs en busca de amenazas.

"""
import os
from funcion import menu

if __name__ == "__main__":
    with open('objetivo/ip.txt', 'r') as archivo_ip:
        lista_ip = archivo_ip.read().splitlines()
    
    with open('objetivo/dominio.txt', 'r') as archivo_dominio:
        lista_dominio = archivo_dominio.read().splitlines()
    
    with open('objetivo/hash.txt', 'r') as archivo_hash:  
        lista_hash = archivo_hash.read().splitlines()  
    
    menu.run_menu(lista_ip, lista_dominio, lista_hash) 
# PyVTInspeKtor/PyVTInspeKtor.py
