#!C:\Users\Personal\AppData\Local\Programs\Python\Python37\python.exe

import cgi;
import cgitb; cgitb.enable()
import sys
from io import TextIOWrapper
sys.stdout = TextIOWrapper(sys.stdout.buffer.detach(), encoding='utf8')
from publicar_mascota_save_data import PublicarMascotaDatabase
print("Content-type: text/html\r\n\r\n")
pmdb=PublicarMascotaDatabase("root","")
domicilio=pmdb.get_five()
a= '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="estilos.css">

    <title>Inicio</title>
    <style>
        
        td >div {
        height:100%;
        width:100%;
        overflow-y:scroll;
        
        }
        td a {
            display: block;
            
        }

        tr:nth-child(even) {
            background-color: white;
        }

        thead {
            background-color: #242424;
            border-bottom: solid 5px #b2b2b2;
            border-top: solid 5px #242424;
            color: white;

        }

        td, th {
            border: 0;
            border-bottom: solid 2px #b2b2b2;
            
        }

        .ListadoMascotas {
            border: 0;
            margin-left: 5%;
            background-color: #ddd;
            width: 90%;
        }

        @media screen and (max-width: 766px) {

            .ListadoMascotas {
                margin-left: 0;
                width: 100%;

            }

            /* Desaparecer el header */
            table.ListadoMascotas thead, th {
                border: none;
                clip: rect(0, 0, 0, 0);
                height: 1px;
                margin: -1px;
                overflow: hidden;
                padding: 0;
                position: absolute;
                width: 1px;
            }

            table.ListadoMascotas tr {
                border-bottom: 3px solid;
            }

            table.ListadoMascotas td {
                border-bottom: 1px solid #ddd;
                display: block;
                font-size: 1.2em;
                text-align: right;
                padding: 10px;
            }

            table.ListadoMascotas td:last-child {
                padding-bottom: 200px;
            }

            .fotos {
                width: 79px;
            }

            table.ListadoMascotas td:before {
                content: attr(data-label);
                float: left;
                color: black;
                font-weight: bold;
                font-size: 1em;
            }

            table.ListadoMascotas td:last-child {
                text-align: center;
            }


        }

    </style>
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
                <li><a href="Informar.html">Informar Mascotas
                </a></li>
                <li><a href="ver_listado.py">Ver Listado de Mascotas</a></li>
                <li><a href="Estadísticas.html">Estadísticas</a></li>
            </ul>
        </nav>
    </div>
</header>
<div>
    <section id="banner">
        <img src="mascotas.jpg" alt="banner">
        <div class="contenedorbanner">
            <h2>Bienvenid@s</h2>
            <p>
                Ayúdanos a censar a nuestras mascotas!
            </p>
        </div>
    </section>
</div>

<div class="títulos"><h1>¡Conoce a las últimas mascotas registradas!</h1></div>

<div class="contenedorTabla">
    <table class="ListadoMascotas">
        <thead>
        <tr>
            <th>Comuna</th>
            <th>Calle</th>
            <th>Tipo-Cantidad</th>
            <th>Foto</th>
        </tr>
        </thead>'''
print(a)
ultimos=pmdb.get_five() #ultimos 5 domicilios

for u in ultimos:
    fila=f'''
        <tbody>
        <tr>
            <td data-label="Comuna">{pmdb.get_comuna(u[2])[0]}</td>
            <td data-label="Calle">{u[3]}</td>
            <td data-label="Tipo-Cantidad">
        '''
    print(fila)

    mascotas=pmdb.tipoCantidad(u[0])# tipo y cantidad de cada mascota en el domicilio
    for m in mascotas:
        tipo_cantidad=f'''
                <a>{pmdb.tipo_mascota(m[0])[0]}-{m[1]}</a>
                '''
        print(tipo_cantidad)
    print('</td><td class="scroll" data-label="Foto"><div class="fotitos">')
    fotos=pmdb.fotos_domicilio(u[0]) #todas las fotos del domicilio
    for f in fotos:
        fotitos=f'''
               <img class="fotos" src="img/{f[0]}" alt="mascota" width="100">
            '''
        print(fotitos)
fin='''
        </div>
        </td>
            </tr>
            </tbody>'''
print(fin)
