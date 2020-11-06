#!C:\Users\Personal\AppData\Local\Programs\Python\Python37\python.exe

import cgi;
import cgitb;

cgitb.enable()
import sys
from io import TextIOWrapper

sys.stdout = TextIOWrapper(sys.stdout.buffer.detach(), encoding='utf8')
from publicar_mascota_save_data import PublicarMascotaDatabase

print("Content-type: text/html\r\n\r\n")
pmdb = PublicarMascotaDatabase("root", "")
domicilio = pmdb.get_five()
c = int(pmdb.count_domicilios()[0])
head = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="estilos.css">
    <title>Listado de mascotas</title>
    <script>
        function AbrirInfo(info) {
            document.getElementById(info).style.display = "block";
            document.getElementById('cerrarInfo').style.display = "block";
        }

        function cerrar() {
            document.getElementById('cerrarInfo').style.display = "none";
            var infos = document.getElementsByClassName('InfoMascotas')
            for (var i = 0; i < infos.length; i++) {
                infos[i].style.display = "none";
            }
        }
    </script>
<style>
    .siguiente .buttonVolver {
        margin-left:77%
    }
    #cerrarInfo {
        display: none;
        position: absolute;
        left: 77%;
        top: 22%;
        padding: 20px;
    }
    td a {
        display: block;
    }
    tr:nth-child(even) {
        background-color: white;
    }
    thead {
        background-color: #242424;
        border-bottom: solid 8px #b2b2b2;
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
    tr:hover td {
        background-color: #92ff63;
        cursor: pointer;
    }
    .InfoMascotas {
        display: none;
        Background: #ddd;
        width: 60%;
        color: #000000;
        padding: 50px;
        border-radius: 22px;
        position: absolute;
        left: 15%;
        top: 25%;
        -webkit-box-shadow: 0px 3px 10px 2px rgba(0, 0, 0, 0.75);
        -moz-box-shadow: 0px 3px 10px 2px rgba(0, 0, 0, 0.75);
        box-shadow: 0px 3px 10px 2px rgba(0, 0, 0, 0.75);
    }
    .cerrarFoto{
        display: none;
        color: blue;
        text-decoration-line: underline;
        font-size: 25px;
    }
    .cerrarFoto:hover{
        cursor: pointer;
    }



    @media screen and (max-width: 766px) {
        #cerrarInfo {
        display: none;
        position: absolute;
        left: 50%;
        top: 22%;
        padding: 20px;
    }
        .InfoMascotas {
            left: 0;
            text-align: left;
            width: 100%;
            padding:0;
            padding-left:2%;
        }
        .InfoMascotas .fotoMascota{
            left:0%;
        }

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

        /* Cada celda ocupa todo el ancho
  de la tabla */
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

        @media screen and (max-width: 300px) {
            .InfoMascotas {
                left: 0;
                width: 90%;
            }
        }
    }
</style>
</head>
'''
b1 = '''
<body>
<header class="header">
    <div class="container logo-nav-container">
        <a href="inicio.html" class="logo">
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

<div class="títulos"><h1>Listado de mascotas</h1></div>
<div class="contenedorTabla">
    <table class="ListadoMascotas">
        <thead>
        <tr>
            <th>Fecha ingreso</th>
            <th>Comuna</th>
            <th>Nombre calle</th>
            <th>Nombre contacto</th>
            <th>Total mascotas</th>
            <th>Total fotos</th>
        </tr>
        </thead>
'''
print(head)
print(b1)
x = ''
for d in domicilio:
    x = int(d[0])  # guardará la id de la ultima fila
    fila = f'''
    <tbody>
        <tr onclick="location.href='información.py?i={d[0]}'">
            <td data-label="Fecha ingreso">{str(d[1])}</td>
            <td data-label="Comuna">{pmdb.get_comuna(d[2])[0]}</td>
            <td data-label="Nombre calle">{d[3]}</td>
            <td data-label="Nombre contacto">{str(d[6])}</td>
            <td data-label="Total mascotas">{pmdb.count_pets(d[0])[0]}</td>
            <td data-label="Total fotos">{pmdb.count_pics(d[0])[0]}</td>
        </tr>
    '''
    print(fila)

b2 = '''
    </tbody>
</table>'''
print(b2)

if c > 5:
    boton = f'''
    <p></p>
    <div class="siguiente">
    <button class="buttonVolver" onclick="location.href='siguiente.py?i={x}'">Ver más</button>
    </div>
    <p></p>
    </html>
    '''
    print(boton)

b3 = '''
<p></p>
</html>
'''
print(b3)
