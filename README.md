# PyVTInspeKtor
PyVTInspeKtor es una herramienta de seguridad que permite a los usuarios escanear y analizar diferentes tipos de objetivos en busca de amenazas y malwares utilizando la API de VirusTotal, que es un servicio de análisis de seguridad en línea. El proyecto está diseñado para ser ejecutado desde la línea de comandos y ofrece varias opciones para analizar diferentes tipos de datos.

[![stars](https://custom-icon-badges.demolab.com/github/stars/DenverCoder1/custom-icon-badges?logo=star)](https://github.com/DenverCoder1/custom-icon-badges/stargazers "stars")
[![issues](https://custom-icon-badges.demolab.com/github/issues-raw/DenverCoder1/custom-icon-badges?logo=issue)](https://github.com/DenverCoder1/custom-icon-badges/issues "issues")
[![license](https://custom-icon-badges.demolab.com/github/license/denvercoder1/custom-icon-badges?logo=law&logoColor=white)](https://github.com/DenverCoder1/custom-icon-badges/blob/main/LICENSE?rgh-link-date=2021-08-09T18%3A10%3A26Z "license MIT")
[![discord](https://custom-icon-badges.demolab.com/discord/819650821314052106?color=7289DA&logo=comments&label=discord&logoColor=white)](https://discord.gg/fPrdqh3Zfu "Dev Pro Tips Discussion & Support Server")

## ⚡ Estructura

PyVTInspeKtor/
├── funcion/
│   ├── menu.py
│   ├── def_ip.py
│   ├── def_dominio.py
│   ├── def_hash.py
│   └── key.py
├── reporte/
│   ├── (archivos de informes generados)
├── objetivo/
│   ├── ip.txt
│   ├── dominio.txt
│   └── hash.txt
└── PyVTInspeKtor.py

## ⚡ Como usarlo

El usuario inicia la aplicación desde la línea de comandos utilizando PyVTInspeKtor.py.
Selecciona el tipo de escaneo que desea realizar (IP, dominio o hash).
Proporciona la lista de objetivos que se escanearán.
La aplicación utiliza la API de VirusTotal para analizar los objetivos y genera un informe.
El informe se guarda en un archivo de texto para su revisión posterior.

## 🚀 Características claves

Escanear IPs: Permite a los usuarios escanear una lista de direcciones IP en busca de posibles amenazas. Después del escaneo, se genera un informe que indica si una IP es maliciosa o no.

Escanear Dominios: Ofrece la capacidad de escanear una lista de dominios en busca de amenazas en línea. Los resultados se almacenan en un informe que muestra si un dominio es malicioso o seguro.

Escanear Hashes: Permite a los usuarios escanear una lista de hashes de archivos para verificar si son maliciosos o no. El resultado se presenta en un informe que indica si un hash está relacionado con malware.

Generación de Informes: PyVTInspeKtor genera informes detallados después de cada escaneo, lo que facilita la revisión de los resultados de seguridad.

## 🤗 Contribución


## 💬 Preguntas?



## 🤩 Reporte de problemas?


## 👨‍💻 Componentes del Proyecto
Componentes del Proyecto:

PyVTInspeKtor.py: El archivo principal que inicia la aplicación y maneja la interacción con el usuario.
menu.py: Contiene la interfaz de línea de comandos y las opciones de menú para que los usuarios seleccionen el tipo de escaneo.
def_ip.py: Contiene funciones para escanear direcciones IP y generar informes.
def_dominio.py: Contiene funciones para escanear dominios y generar informes.
def_hash.py: Contiene funciones para escanear hashes de archivos y generar informes.
key.py: Almacena la clave de API de VirusTotal utilizada para realizar los escaneos.
reporte: Una carpeta donde se almacenan los informes generados después de cada escaneo.
