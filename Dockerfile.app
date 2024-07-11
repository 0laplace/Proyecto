# Dockerfile.app
FROM python:3.9-alpine

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto
COPY . .

# Comando por defecto para ejecutar el contenedor
CMD ["python", "create_table.py"]
