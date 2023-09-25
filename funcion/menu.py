# PyVTInspeKtor/funcion/menu.py
import os
import time
from . import def_ip, def_dominio, def_hash
from funcion import def_ip, def_dominio, def_hash

LISTA_MALICIOSA = []

def display_menu():
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║      👨‍💻 Menú de OSIN Kuardian 👨‍💻      ║")
    print("╠══════════════════════════════════════════╣")
    print("║ 1️⃣  Escanear Lista de IP                  ║")
    print("║ 2️⃣  Escanear Lista de Dominios            ║")
    print("║ 3️⃣  Escanear Lista de Hashes              ║")
    print("║ 4️⃣  Salir                                 ║")
    print("╚══════════════════════════════════════════╝")

def clear_screen():
    # Esta función limpia la pantalla de la terminal para una presentación más limpia
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_choice():
    while True:
        try:
            choice = int(input("Por favor, seleccione una opción (1/2/3/4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

def run_menu(lista_ip, lista_dominio, lista_hash): 
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            clear_screen()
            print("Has seleccionado escanear Lista de IP.")
            for ip in lista_ip:
                print(f"Escaneando {ip} en 20 segundos...")
                cantidad_maliciosa = def_ip.escanear_ip(ip)
                if cantidad_maliciosa > 0:
                    LISTA_MALICIOSA.append(ip)
                time.sleep(20)  # Esperar 20 segundos entre escaneos
            clear_screen()  # Limpia la pantalla después de escanear
        elif choice == 2:
            clear_screen()
            print("Has seleccionado escanear Lista de Dominios.")
            for dominio in lista_dominio:
                print(f"Escaneando Dominio: {dominio} en 20 segundos...")
                cantidad_maliciosa = def_dominio.escanear_dominio(dominio)
                if cantidad_maliciosa > 0:
                    LISTA_MALICIOSA.append(dominio)
                time.sleep(20)
            clear_screen()
        elif choice == 3:
            clear_screen()
            print("Has seleccionado escanear Lista de Hashes.")
            for hash_value in lista_hash:
                print(f"Escaneando Hash: {hash_value} en 20 segundos...")
                cantidad_maliciosa = def_hash.escanear_hash(hash_value)
                if cantidad_maliciosa > 0:
                    LISTA_MALICIOSA.append(hash_value)
                time.sleep(20)
            clear_screen()
        elif choice == 4:
            clear_screen()
            print("Saliendo del programa.")
            break
