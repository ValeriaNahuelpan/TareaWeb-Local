#!C:\Users\Personal\AppData\Local\Programs\Python\Python37\python.exe
import mysql.connector
#acá se encuentran todas las consultas que se usaron
class PublicarMascotaDatabase:

    def __init__(self, user, password):
        self.db = mysql.connector.connect(
           host ="localhost",
           user="root",
           password="",
           database="tarea2",

        )
        self.cursor = self.db.cursor()

    def save_data1(self, data):
        sql ='''
            INSERT INTO domicilio (fecha_ingreso,comuna_id,nombre_calle, numero, sector, nombre_contacto, email, celular)
             VALUES (NOW(),(SELECT id FROM comuna WHERE nombre=%s), %s, %s, %s, %s, %s, %s);
            '''
        self.cursor.execute(sql, data)  # ejecuto la consulta
        self.db.commit()  # modifico la base de datos

    def save_data2(self,data):
        sql = '''
              INSERT INTO mascota_domicilio (tipo_mascota_id, edad, color, raza, esterilizado, vacunas_al_dia, domicilio_id)
              VALUES (%s, %s, %s, %s, %s, %s, (SELECT MAX(id) FROM domicilio));
              '''

        self.cursor.execute(sql, data)  # ejecuto la consulta
        self.db.commit()  # modifico la base de datos
    def save_photo(self,data):
        sql = '''
                      INSERT INTO foto_mascota (ruta_archivo, nombre_archivo,  mascota_domicilio_id)
                      VALUES (%s, %s, (SELECT MAX(id) FROM mascota_domicilio));
                      '''
        self.cursor.execute(sql, data)  # ejecuto la consulta
        self.db.commit()  # modifico la base de datos
    def get_all(self, tablename):
        self.cursor.execute(f'SELECT * FROM {tablename}')
        return self.cursor.fetchall()
    def get_five(self):
        self.cursor.execute(f'SELECT id, fecha_ingreso, comuna_id, nombre_calle, numero, sector, nombre_contacto, email, celular FROM domicilio ORDER BY fecha_ingreso DESC LIMIT 5')
        return self.cursor.fetchall()

    def siguientes(self):
        self.cursor.execute(
            f'SELECT id, fecha_ingreso, comuna_id, nombre_calle, numero, sector, nombre_contacto, email, celular FROM domicilio ORDER BY fecha_ingreso DESC LIMIT 5 OFFSET 5')
        return self.cursor.fetchall()
    def get_comuna(self,id): # entrega la comuna dada una id
        self.cursor.execute(
            f'SELECT nombre FROM comuna WHERE id={id}')
        return self.cursor.fetchone()
    def count_pets(self,id): #cuenta la cantidad de mascotas ingresadas en un domicilio
        self.cursor.execute(
            f'SELECT COUNT(id) FROM mascota_domicilio WHERE domicilio_id={id}')
        return self.cursor.fetchone()
    def count_pics(self,id):#cuenta la cantidad de imagenes por domicilio
        self.cursor.execute(
            f'SELECT COUNT(id) FROM foto_mascota WHERE mascota_domicilio_id IN (SELECT id FROM mascota_domicilio WHERE domicilio_id={id})')
        return self.cursor.fetchone()
    def count_domicilios(self): #cuenta filas de una tabla
        self.cursor.execute(
            f'SELECT COUNT(id) FROM domicilio')
        return self.cursor.fetchone()
    def siguientess(self,id):#muestra todas las filas despues de una id dada
        self.cursor.execute(
            f'SELECT id, fecha_ingreso, comuna_id, nombre_calle, numero, sector, nombre_contacto, email, celular FROM domicilio WHERE id<{id} ORDER BY fecha_ingreso DESC')
        return self.cursor.fetchall()
    def row(self,id):# entrega una fila de un domicilio dada su id
        self.cursor.execute(
            f'SELECT id, fecha_ingreso, comuna_id, nombre_calle, numero, sector, nombre_contacto, email, celular FROM domicilio WHERE id={id}')
        return self.cursor.fetchall()
    def mascotas(self,id):#entrega las mascotas dada la id del domicilio
        self.cursor.execute(
            f'SELECT id,tipo_mascota_id, edad, color, raza, esterilizado, vacunas_al_dia FROM mascota_domicilio WHERE domicilio_id={id}')
        return self.cursor.fetchall()
    def tipo_mascota(self,id):#entrega el tipo de mascota dada la id
        self.cursor.execute(
            f'SELECT nombre FROM tipo_mascota WHERE id={id}')
        return self.cursor.fetchone()
    def region(self,id): #region de un domicilio
        self.cursor.execute(
            f'SELECT nombre FROM region WHERE id IN (SELECT region_id FROM comuna WHERE id in (SELECT comuna_id from domicilio WHERE id={id}))')
        return self.cursor.fetchone()
    def fotos(self,id):#entrega los nombres de las fotos dada la id de la mascota
        self.cursor.execute(
            f'SELECT id,nombre_archivo FROM foto_mascota WHERE mascota_domicilio_id ={id}')
        return self.cursor.fetchall()
    def totalfotos(self):#entrega el total de fotos
        self.cursor.execute(
            f'SELECT count(*) FROM foto_mascota')
        return self.cursor.fetchall()
    def delete(self):# borra el ultimo registro uwu
        self.cursor.execute(
            f'DELETE FROM foto_mascota WHERE mascota_domicilio_id IN (SELECT id FROM mascota_domicilio WHERE domicilio_id IN (SELECT MAX(id) FROM domicilio))')
        self.db.commit()
        self.cursor.execute(
            f'DELETE  FROM mascota_domicilio WHERE domicilio_id IN (SELECT MAX(id) FROM domicilio)')
        self.db.commit()
        self.cursor.execute(
            f'DELETE FROM domicilio WHERE id IN (SELECT MAX(id) FROM domicilio)')
        self.db.commit()
    def tipoCantidad(self,id):#entrega los tipos y cantidad de mascotas que hay en un domicilio dada la id
        self.cursor.execute(
            f'SELECT tipo_mascota_id,count(tipo_mascota_id) FROM mascota_domicilio WHERE domicilio_id={id} GROUP BY tipo_mascota_id')
        return self.cursor.fetchall()
    def fotos_domicilio(self,id):#entrega los nombres de las fotos del domicilio
        self.cursor.execute(
            f'SELECT nombre_archivo FROM foto_mascota WHERE mascota_domicilio_id IN (SELECT id FROM mascota_domicilio WHERE domicilio_id={id}) ')
        return self.cursor.fetchall()
    def id_ultimo_domicilio(self):
        self.cursor.execute(
            f'SELECT MAX(id) FROM domicilio')
        return self.cursor.fetchone()






