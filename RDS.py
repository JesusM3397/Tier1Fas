import psycopg2

# Parámetros de conexión a la base de datos
db_host = "your-db-hostname.cabcdefghijklmnopq.us-east-1.rds.amazonaws.com"
db_port = 5432  # Puerto predeterminado de PostgreSQL
db_name = "your-db-name"
db_user = "your-db-username"
db_password = "your-db-password"

try:
    # Conexión a la base de datos
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )

    # Crear un cursor
    cursor = connection.cursor()

    # Ejemplo de consulta
    cursor.execute("SELECT * FROM your_table_name")
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print("Error al conectarse a la base de datos:", e)

