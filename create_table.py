import sqlite3

def create_process_table():
    # Conectar a la base de datos (creará el archivo si no existe)
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Sentencia SQL para crear la tabla
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS Process (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        execution_date DATE NOT NULL,
        summary_file VARCHAR(255) NOT NULL,
        etl_file VARCHAR(255) NOT NULL,
        detail_file VARCHAR(255) NOT NULL
    );
    """

    # Ejecutar la sentencia SQL
    cursor.execute(create_table_sql)

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()
    print("Tabla 'Process' creada con éxito")

if __name__ == "__main__":
    create_process_table()
