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

# Función para generar el resumen diario en CSV
def generate_summary(data_file):
    # Leer el archivo JSON de datos
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    # Ejemplo de cálculo de resumen (aquí puedes adaptarlo según tus necesidades)
    total_users = len(data)
    
    # Crear el nombre del archivo de resumen
    summary_filename = os.path.join(output_directory, f"summary_{date.today().strftime('%Y%m%d')}.csv")
    
    # Escribir el resumen en el archivo CSV
    with open(summary_filename, 'w', newline='') as csvfile:
        fieldnames = ['Metric', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow({'Metric': 'Total Users', 'Value': total_users})
        
    print(f"Resumen diario guardado en: {summary_filename}")

    # Guardar los datos en la base de datos
    save_to_database(summary_filename)

# Función para guardar los datos en la base de datos
def save_to_database(summary_file):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Process (execution_date, summary_file, etl_file, detail_file) VALUES (?, ?, ?, ?)",
                   (date.today(), summary_file, '', ''))

    conn.commit()
    conn.close()
    print("Datos guardados en la base de datos")

# Llamar a la función con el archivo de datos JSON
data_file = 'C:\\Users\\trafa\\OneDrive\\Documentos\\Proyecto\\json\\data_20240710.json'
generate_summary(data_file)
