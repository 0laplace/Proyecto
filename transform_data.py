import os
import csv
import json
import sqlite3
from datetime import date
from dotenv import load_dotenv, find_dotenv

# Cargar variables de entorno desde el archivo .env
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Ruta donde se guardarán los archivos CSV
output_directory = os.getenv("OUTPUT_DIRECTORY", "C:\\Users\\trafa\\OneDrive\\Documentos\\Proyecto\\json")

# Función para transformar datos JSON a CSV
def transform_to_csv(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Crear el nombre del archivo CSV
    csv_filename = os.path.join(output_directory, f"ETL_{date.today().strftime('%Y%m%d')}.csv")

    # Escribir los datos en el archivo CSV
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Name', 'Email', 'Gender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in data['users']:
            writer.writerow({
                'ID': item['id'],
                'Name': item['firstName'] + ' ' + item['lastName'],
                'Email': item['email'],
                'Gender': item['gender']
            })
    
    print(f"Datos transformados guardados en: {csv_filename}")

    # Guardar los datos en la base de datos
    save_to_database(csv_filename)

# Función para guardar los datos en la base de datos
def save_to_database(etl_file):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE Process SET etl_file = ? WHERE execution_date = ?",
                   (etl_file, date.today()))

    conn.commit()
    conn.close()
    print("Datos transformados guardados en la base de datos")

# Llamar a la función con el archivo JSON
json_file = 'C:\\Users\\trafa\\OneDrive\\Documentos\\Proyecto\\json\\data_20240710.json'
transform_to_csv(json_file)
