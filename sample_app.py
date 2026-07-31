from flask import Flask
from flask import request
from flask import render_template
import pymysql

sample = Flask(__name__)

@sample .route ("/")
def main():
	try:
		conn=pymysql.cocconnect(host="servidor-bd-082",user="root" ,passwd="sena123", db= "082_db",port=5051, debug=True)
		conn.close()
		db_status = "Conexión exitosa a la base de datos"
	except Exception as e:
		db_status = f"Error al conectar a la base de datos: {e}"
	return f"<h1>mi app </h1><p>{db_status}</p>"


if __name__ == "__main__":
	sample.run (host="data-082", port=5050, debug=True)