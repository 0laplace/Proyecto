import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Ejecutar una consulta para verificar la tabla 'Process'
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Process';")

# Verificar si la tabla existe
table_exists = cursor.fetchone()

if table_exists:
    print("La tabla 'Process' existe en la base de datos.")
else:
    print("La tabla 'Process' no existe en la base de datos.")

# Cerrar la conexión
conn.close()
