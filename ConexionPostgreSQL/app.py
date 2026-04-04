"""Importamos la librerria psycode2 para establecer la conecxión con la db"""

import os  # Importa el módulo os para acceder a variables de entorno
import psycopg2  # Importa psycopg2 para conectar con PostgreSQL
from psycopg2 import (
    OperationalError,  # Importa excepciones específicas de psycopg2
    Error,
)
from dotenv import (
    load_dotenv,  # Importa la función para cargar variables de entorno desde .env
)

# de las variables de entorno

load_dotenv()  # Carga las variables de entorno desde el archivo .env
# Establecemos una conexión
conn = None  # Inicializa la variable de conexión como None

DB_NAME = os.getenv(
    "DB_NAME"
)  # Obtiene el nombre de la base de datos desde variables de entorno
DB_USER = os.getenv("DB_USER")  # Obtiene el nombre del usuario
DB_PASSWORD = os.getenv("DB_PASSWORD")  # Obtiene la contraseña
DB_HOST = os.getenv("DB_HOST")  # Obtiene el host (ej. 127.0.0.1)
DB_PORT = os.getenv("DB_PORT")  # Obtiene el puerto
"""Usamos la librerira psycopg2 y el método connect para establecer 
la conexión"""


def conectar():
    """Establece una conexión con la base de datos PostgreSQL.

    Returns:
        psycopg2.connection or None: La conexión si es exitosa, None si falla.
    """
    try:
        conn = psycopg2.connect(  # Intenta conectar a la base de datos con los parámetros proporcionados
            dbname=DB_NAME,  # Nombre de la base de datos
            user=DB_USER,  # Nombre del usuario
            password=DB_PASSWORD,  # Contraseña del usuario
            host=DB_HOST,  # Dirección del host
            port=DB_PORT,  # Puerto de conexión
        )
        print("Coneción OK")  # Imprime mensaje de conexión exitosa
        return conn  # Retorna la conexión establecida
    except OperationalError as oe:  # Captura errores operacionales de conexión
        print(
            f"[ERROR] Problema operacional al conectar: {oe}"
        )  # Imprime el error operacional
    except Error as e:  # Captura otros errores de psycopg2
        print(
            f"[ERROR] Problema operacional al conectar: {e}"
        )  # Imprime el error general
    except Exception as ex:  # Captura cualquier excepción inesperada
        print(f"[ERRRO] Inesperado: {ex}")  # Imprime el error inesperado
    return None  # Retorna None si la conexión falla


def llamar_profesores(conn):
    """Obtiene y muestra los nombres de los profesores de la base de datos.

    Args:
        conn (psycopg2.connection): La conexión a la base de datos.
    """
    query = """SELECT first_name FROM teachers"""  # Define la consulta SQL para seleccionar los nombres de los profesores
    try:
        with conn.cursor() as cur:  # Crea un cursor para ejecutar la consulta
            cur.execute(query)  # Ejecuta la consulta
            fila = cur.fetchall()  # Obtiene todas las filas resultantes
            for f in fila:  # Itera sobre cada fila
                print(f)  # Imprime el nombre del profesor
    except Error as e:  # Captura errores de psycopg2
        print(
            f"[ERRROR] No se pudieron recuperar los profesores: {e}"
        )  # Imprime el error


def insert_teacher(
    conn,
    department_id,
    first_name,
    last_name,
    email,
    phone,
    hire_date,
    salary,
):
    """Inserta un nuevo profesor en la base de datos.

    Args:
        conn (psycopg2.connection): La conexión a la base de datos.
        department_id (int): ID del departamento.
        first_name (str): Nombre del profesor.
        last_name (str): Apellido del profesor.
        email (str): Correo electrónico.
        phone (str): Número de teléfono.
        hire_date (str): Fecha de contratación (formato YYYY-MM-DD).
        salary (str): Salario.
    """
    query = """INSERT INTO teachers(department_id, first_name, last_name, email, phone, hire_date, salary)
VALUES(%s, %s, %s, %s, %s, %s, %s);"""  # Define la consulta SQL para insertar un profesor
    params = (
        department_id,
        first_name,
        last_name,
        email,
        phone,
        hire_date,
        salary,
    )  # Parámetros para la consulta
    try:
        with conn.cursor() as cur:  # Crea un cursor para ejecutar la consulta
            cur.execute(query, params)  # Ejecuta la consulta con parámetros
        conn.commit()  # Confirma los cambios en la base de datos
        print("[OK] Inserción segura realizada")  # Imprime mensaje de éxito
    except Error as e:  # Captura errores de psycopg2
        conn.rollback()  # Revierte los cambios en caso de error
        print(f"[ERROR] No de pudo insertar el profesor: {e}")  # Imprime el error


conexion = conectar()  # Llama a la función para establecer la conexión
insert_teacher(  # Llama a la función para insertar un profesor
    conexion,  # Pasa la conexión
    5,  # ID del departamento
    "Adriana",  # Nombre
    "Rivera",  # Apellido
    "Rivera@adri",  # Email
    "123454987",  # Teléfono
    "2023-05-15",  # Fecha de contratación
    "1500000",  # Salario
)
