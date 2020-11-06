#!C:\Users\Personal\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-
import cgi;
import cgitb;

cgitb.enable()
from publicar_mascota_save_data import PublicarMascotaDatabase
import os
import cgitb;

cgitb.enable(display=0, logdir='.')  # mostrar los erroes en un archivo html
import sys
from io import TextIOWrapper

sys.stdout = TextIOWrapper(sys.stdout.buffer.detach(), encoding='utf8')
print("Content-type: text/html\r\n\r\n")

form = cgi.FieldStorage()
pmdb = PublicarMascotaDatabase("root", "")

html = f'''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="estilos.css">
    <title>Gracias</title>
</head>
<body>
<header class="header">
    <div class="container logo-nav-container">
        <a href="portada.py" class="logo">
            <img src="pata.png" width="30" height="30" alt="logo">
            MundoPets!
            <img src="pata.png" width="30" height="30" alt="logo">
        </a>

        <span class="menu-icon"><img src="menu.png" width="30" height="30" alt="menu-icono"></span>
        <nav class="navigation">
            <ul class="show">
                <li><a href="Informar.html">Informar Mascotas</a></li>
                <li><a href="ver_listado.py">Ver Listado de Mascotas</a></li>
                <li><a href="Estadísticas.html">Estadísticas</a></li>
            </ul>
        </nav>
    </div>
</header>
'''
print(html)
h = '''
    <div class="títulos">
    <h1>Hemos recibido su información,</h1>
    <h1>¡gracias por colaborar!</h1>
    </div>
    <div class="volver">
    <button class="buttonVolver" onclick="location.href='portada.py'"> volver a la portada</button>
    </div>
    </body>
    </html>
    '''#cambiará si la informacion enviada fué incorrecta


def guardardomicilio():  # los campos sector y celular son opcionales entonces la data a guardar depende de ello
    if 'sector' and 'celular' not in form:
        return (form['Comuna'].value, form['calle'].value, form['numero'].value,
                None, form['nombre'].value,
                form['email'].value, None)
    elif 'sector' not in form:
        return (form['Comuna'].value, form['calle'].value, form['numero'].value,
                None, form['nombre'].value,
                form['email'].value, form['celular'].value)
    elif 'celular' not in form:
        return (form['Comuna'].value, form['calle'].value, form['numero'].value,
                form['sector'].value, form['nombre'].value,
                form['email'].value, None)
    else:
        return (form['Comuna'].value, form['calle'].value, form['numero'].value,
                form['sector'].value, form['nombre'].value,
                form['email'].value, form['celular'].value)

pmdb.save_data1(guardardomicilio())
id=pmdb.id_ultimo_domicilio()[0]
i = 1
while (i > 0):
    if 'tipo-mascota' + str(i) in form:  # agregamos la mascota i a la base de datos
        data2 = (
            form['tipo-mascota' + str(i)].value, form['edad-mascota' + str(i)].value,
            form['color-mascota' + str(i)].value,
            form['raza-mascota' + str(i)].value, form['esterilizado-mascota' + str(i)].value,
            form['vacunas-mascota' + str(i)].value)
        pmdb.save_data2(data2)
        j = 1
        filename = ''
        while (j > 0):  # guardamos las fotos de la mascota i
            if 'foto-mascota' + str(i) + str(j) in form:
                foto = form['foto-mascota' + str(i) + str(j)]  # binario del archivo recibido
                filename = foto.filename
                if '.png' in filename or '.jpg' in filename or '.JPG' in filename or '.PNG' in filename:  # validacion formatos permitidos
                    fn = os.path.basename(filename)  # obtener nombre base del archivo
                    open('img/' + str(id)+str(i)+str(j)+'.jpj', 'wb').write(foto.file.read())  # guarda archivo renombrado en el servidor
                    datafoto = ('img/' + str(id)+str(i)+str(j), str(id)+str(i)+str(j)+'.jpj') #el nombre que se guarda es id_domicilio+ nro de mascota + cantidad de foto
                    pmdb.save_photo(datafoto)
                    j = j + 1
                else: #no guarda la informacion ingresada si el archivo no tiene el formato pedido
                    pmdb.delete()#borra lo que ya se habia guardado
                    h='''
                    <div class="títulos">
                    <h1>No se guardó su información :( </h1>
                    <h1>Se ingresó un archivo que no era una foto >:c </h1>
                    </div>
                    <div class="volver">
                    <button class="buttonVolver" onclick="location.href='Informar.html'"> volver a intentarlo</button>
                    </div>
                    </body>
                    </html>
                    '''
                    break
            else:
                break
        i = i + 1  # avanzo para ver si hay otra mascota

    else:  # si nos pasamos de la cantidad de mascotas ingresadas entonces se termina el ciclo
        break
print(h) #imprime el mensajito que dice gracias o que no se pudo enviar el formulario
