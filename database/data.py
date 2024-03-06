import mysql.connector
db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="1234",
                                     port=3306,
                                     autocommit=True
                                    )
cursor = db.cursor(dictionary=True)

def databaseConnect():
        cursor.execute("CREATE database IF NOT EXISTS discord")
        cursor.execute("USE discord")
        cursor.execute("CREATE table IF NOT EXISTS reportes (id_afectado varchar(100) PRIMARY KEY,infraccion varchar(100))")
        cursor.execute("CREATE table IF NOT EXISTS servidores (id varchar(19) PRIMARY KEY,nombre varchar(100))")
        cursor.execute("CREATE table IF NOT EXISTS rolRainbow (idRol varchar(100) PRIMARY KEY,idServidor varchar(100))")
        cursor.execute("ALTER TABLE rolRainbow ADD FOREIGN KEY (idServidor) REFERENCES servidores(id);")