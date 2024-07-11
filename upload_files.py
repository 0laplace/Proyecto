
import os
from dotenv import load_dotenv, find_dotenv
import paramiko
from datetime import date

# Cargar variables de entorno desde el archivo .env
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Acceder a las variables de entorno
sftp_host = os.getenv("SFTP_HOST")
sftp_user = os.getenv("SFTP_USER")
sftp_password = os.getenv("SFTP_PASSWORD")
output_directory = os.getenv("OUTPUT_DIRECTORY", "C:\\Users\\trafa\\OneDrive\\Documentos\\Proyecto\\json")

# Función para subir un archivo al SFTP
def upload_to_sftp(file_path):
    try:
        transport = paramiko.Transport((sftp_host, 22))
        transport.connect(username=sftp_user, password=sftp_password)
        sftp = transport.open_sftp()
        sftp.put(file_path, f'/remote_path/{os.path.basename(file_path)}')
        sftp.close()
        transport.close()
        print(f"Archivo {file_path} subido al SFTP")
    except Exception as e:
        print(f"Error al subir el archivo {file_path}: {e}")

# Subir los archivos generados al SFTP
files_to_upload = [
    os.path.join(output_directory, f"data_{date.today().strftime('%Y%m%d')}.json"),
    os.path.join(output_directory, f"ETL_{date.today().strftime('%Y%m%d')}.csv"),
    os.path.join(output_directory, f"summary_{date.today().strftime('%Y%m%d')}.csv")
]

for file in files_to_upload:
    upload_to_sftp(file)
