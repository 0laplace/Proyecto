# main.py

from dotenv import load_dotenv, find_dotenv
import os
import requests
import json
from datetime import date
import sqlite3
from cryptography.fernet import Fernet
import paramiko

# Cargar variables de entorno desde el archivo .env
dotenv_path = find_dotenv()
if not dotenv_path:
    print("No se encontró el archivo .env")
else:
    print(f"Archivo .env encontrado en: {dotenv_path}")
    load_dotenv(dotenv_path)

# Acceder a las variables de entorno
sftp_host = os.getenv("SFTP_HOST")
sftp_user = os.getenv("SFTP_USER")
sftp_password = os.getenv("SFTP_PASSWORD")
database_url = os.getenv("DATABASE_URL")

# Imprimir las variables de entorno para verificar
print(f"SFTP Host: {sftp_host}")
print(f"SFTP User: {sftp_user}")
print(f"Database URL: {database_url}")

# Ejemplo de función para obtener datos de la API y guardarlos como JSON
def fetch_data():
    response = requests.get("https://dummyjson.com/users")
    if response.status_code == 200:
        data = response.json()
        with open(f"data_{date.today().strftime('%Y%m%d')}.json", 'w') as f:
            json.dump(data, f)
    else:
        print("Error fetching data")

# Ejemplo de función para encriptar datos
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(file_path, 'wb') as f:
        f.write(encrypted)

# Generar una clave de encriptación (esto debe hacerse una vez y guardarse de forma segura)
# key = Fernet.generate_key()
# print(key)

# Uso de la clave para encriptar un archivo
# encrypt_file('path_to_file', 'your_key_here')

# Ejemplo de función para subir un archivo al SFTP
def upload_to_sftp(file_path):
    transport = paramiko.Transport((sftp_host, 22))
    transport.connect(username=sftp_user, password=sftp_password)
    sftp = transport.open_sftp()
    sftp.put(file_path, f'/remote_path/{os.path.basename(file_path)}')
    sftp.close()
    transport.close()

# Llama a las funciones según sea necesario
fetch_data()
# encrypt_file('data_20230710.json', 'your_key_here')
# upload_to_sftp('data_20230710.json')
