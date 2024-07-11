# importar las bibliotecas necesarias
import os
import requests
import json

from datetime import datetime

# Cargar variables de entorno desde el archivo .env
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if not os.path.exists(dotenv_path):
    print("No se encontró el archivo .env")
    exit(1)

load_dotenv(dotenv_path)

# Acceder a las variables de entorno
api_url = os.getenv("API_URL")  # URL de la API
output_directory = os.getenv("OUTPUT_DIRECTORY")  # Directorio donde guardar los datos

# Función para extraer datos y guardarlos localmente
def extract_data():
    # Obtener la fecha actual
    today_date = datetime.today().strftime('%Y%m%d')

    # Realizar la solicitud a la API
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        # Guardar los datos como JSON localmente
        output_file = os.path.join(output_directory, f"data_{today_date}.json")
        with open(output_file, 'w') as f:
            json.dump(data, f)
        print(f"Datos guardados en: {output_file}")
    else:
        print(f"Error al obtener datos de la API: {response.status_code}")

if __name__ == "__main__":
    extract_data()
