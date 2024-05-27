import mysql.connector

# Configurar la conexión a la base de datos
dbhost = "localhost"
dbuser = "root"
dbpass = ""
dbname = "remaga"

try:
    # Establecer la conexión a la base de datos
    conn = mysql.connector.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)

    # Verificar la conexión
    print("Conectado a la base de datos MySQL 'remaga' exitosamente.")

    # Cerrar la conexión
    conn.close()

except mysql.connector.Error as e:
    print("Error de conexión:", e)
