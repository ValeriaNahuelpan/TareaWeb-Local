#!C:\Users\Personal\AppData\Local\Programs\Python\Python37\python.exe

import cgi;
import cgitb; cgitb.enable()
import sys
from io import TextIOWrapper

sys.stdout = TextIOWrapper(sys.stdout.buffer.detach(), encoding='utf8')
from publicar_mascota_save_data import PublicarMascotaDatabase
print("Content-type: text/html\r\n\r\n")
pmdb=PublicarMascotaDatabase("root","")
datos=cgi.FieldStorage()
i=datos['i'].value
row=pmdb.row(i)
mascotas=pmdb.mascotas(i)
head='''
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
        
    function abrirFoto(id) {
            let i = id.toString();
            document.getElementById(i).style.width="800px";
            document.getElementById(i).style.height="600px";
            document.getElementById('cerrar'+i).style.display="block"
        }
    function cerrarFoto(id) {
        let i=id.toString();
        document.getElementById(i).style.width="320px";
            document.getElementById(i).style.height="240px";
            document.getElementById('cerrar'+i).style.display="none";
    }

    </script>
<style>
    .siguiente{
        margin-left:-50%}
    .siguiente .buttonVolver {
        display: inline-block;
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
        border-bottom: solid 5px #b2b2b2;
        border-top: solid 5px #242424;
        color: white;
    }
    img:hover { cursor:pointer;}

    td, th {
        border: 0;
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
        /* display: none; */
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
b1='''
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
print(head)
print(b1)
region=pmdb.region(i)[0]
for d in row: #es solo un valor d uwu
    b1 = f'''
    <body>
    <div class="InfoMascotas" id="info{d[0]}">
        <h3>Domicilio</h3>
        <p> Region: {region}</p>
        <p>Comuna: {pmdb.get_comuna(d[2])[0]}</p>
        <p>Calle: {d[3]}</p>
        <p>Número: {d[4]}</p>
        <p>Sector:{d[5]}</p>
        <h3>Contacto</h3>
        <p>nombre: {d[6]}</p>
        <p>Email: {d[7]}</p>
        <p>Celular: {d[8]}</p>
     '''
    print(b1)
    for m in mascotas: #imprime informacion de todas las mascotas del domicilio
        b2=f'''
        <h3>Mascota</h3>
        <p>Tipo:{pmdb.tipo_mascota(m[1])[0]}  </p>
        <p>Edad: {m[2]}</p>
        <p>Color: {m[3]}</p>
        <p>Raza: {m[4]}</p>
        <p>Esterilizado: {m[5]} (0=si,1=no,2=no aplica)</p>
        <p>Vacunas al día: {m[6]} (0=si,1=no,2=no aplica)</p>
        '''
        print(b2)
        fotos=pmdb.fotos(m[0]) #fotos de la mascota
        for f in fotos: #imprime todas las fotos de la mascota
            b3=f'''
            <p>Foto:</p>
            <div class="fotoMascota">
            <img  id="{f[0]}" onclick="abrirFoto('{f[0]}')" src="img/{f[1]}" alt="foto" width="320" height="240">
            <p class="cerrarFoto" id="cerrar{f[0]}" onclick="cerrarFoto({f[0]})">cerrar Foto</p>
            </div>
            <body>
            '''
            print(b3)
botones='''
     <div class="siguiente">
    <button class="buttonVolver" onClick="history.go(-1);">Volver </button>
    <button class="buttonVolver" onclick="location.href='portada.py'">Portada</button>
    </div>'''
print(botones)

