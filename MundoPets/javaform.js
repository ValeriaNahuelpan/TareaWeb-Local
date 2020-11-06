/**
 * agrega otra foto



var contfoto = 1;

function agregarOtraFoto(i) {
    /** @type {string}let id = 'entrada' + i;*/
/**
    if (document.getElementsByClassName('foto' + i).length === 4) {// si se agregaron 4 fotos mas, no se permite agregar mas
        return
    }
    let conf = document.getElementById(id); // se agregan mas campos input para agregar fotos
    conf.innerHTML = conf.innerHTML + `
    <div class="entrada" id="${i}${contfoto + 1}">
            <div class="leyenda">Foto</div>
            <input name="foto-mascota" type="file" class="foto${i}" id="foto-mascota${i}${contfoto + 1}" required="required" accept="image/jpeg" >
            <button type="button" id="eliminar${i}${contfoto + 1}" onclick="eliminarfoto(${i}, ${contfoto + 1})"> eliminar</button>
    </div>`;
    contfoto = contfoto + 1;
}
**/

/**
 * agrega otra foto


*/
var contfoto = 1;

function agregarOtraFoto(i) {
    /** @type {string}*/ let id = 'entrada' + i;
    let classlenght=document.getElementsByClassName('foto' + i).length;
    if (document.getElementsByClassName('foto' + i).length === 4) {// si se agregaron 4 fotos mas, no se permite agregar mas
        return
    }
    let conf = document.getElementById(id); // se agregan mas campos input para agregar fotos
    conf.innerHTML = conf.innerHTML + `
    <div class="entrada"  name="${i}${classlenght+2}" id="${i}${classlenght+2}">
            <div class="leyenda">Foto</div>
            <input name="foto-mascota${i}${classlenght+2}" type="file" class="foto${i}" id="foto-mascota${i}${classlenght+2}" required="required" accept="image/jpeg" >
            <button type="button" id="eliminar${i}${classlenght+2}" onclick="eliminarfoto(${i}, ${classlenght+2})"> eliminar</button>
    </div>`;
    contfoto = contfoto + 1;
}
function eliminarfoto(i, j) {
    let a = i.toString();
    let b = j.toString();
    let id = a + b;
    for(var i=0;i<document.getElementsByName(id).length;i++){
        document.getElementsByName(id)[i].style.display="none";
    }
    //document.getElementById(id).style.display = "none";//no muestra el div que agrega otra foto
    document.getElementById('foto-mascota' + id).classList.remove('foto' + a); //le quita la clase para que no se cuente como una foto añadida
}


/**
 * inserta un nuevo formulario
 */
var contadorMascotas = 1;

function AgregarMascota() {
    let a = contadorMascotas.toString();
    let con = document.getElementById('NuevaMascota');
    con.innerHTML = con.innerHTML + `
            <div class="entrada">
            <b>
                Información de mascota ${contadorMascotas + 1}
            </b>
    </div>

        <div class="entrada">
            <div class="leyenda">Tipo-mascota</div>
            <select name="tipo-mascota${contadorMascotas + 1}" id="tipo-mascota${contadorMascotas + 1}" required="required">
                <option value="" selected="selected">Seleccione un tipo</option>
                <option value="1">Perro</option>
                <option value="2">Gato</option>
                <option value="3">Pez</option>
                <option value="4">Tortuga</option>
                <option value="5">Hamster</option>
                <option value="6">Loro</option>
                <option value="7">Iguana</option>
                <option value="8">Araña</option>
            </select>
        </div>

        <div class="entrada">
            <div class="leyenda">Edad en años</div>
            <input name="edad-mascota${contadorMascotas + 1}" type="text" id="edad-mascota${contadorMascotas + 1}"   size="5" />
        </div>
        <div class="entrada">
            <div class="leyenda">Color</div>
            <input name="color-mascota${contadorMascotas + 1}" type="text" id="color-mascota${contadorMascotas + 1}"   size="30" />
        </div>
        <div class="entrada">
            <div class="leyenda">Raza</div>
            <input name="raza-mascota${contadorMascotas + 1}" type="text" id="raza-mascota${contadorMascotas + 1}"   size="30" />
        </div>
        <div class="entrada">
            <div class="leyenda">Esterilizado</div>
            <select name="esterilizado-mascota${contadorMascotas + 1}" id="esterilizado-mascota${contadorMascotas + 1}" required="required">
                <option value="" selected="selected">Seleccione una respuesta</option>
                <option value="0">si</option>
                <option value="1">no</option>
                <option value="2">no aplica</option>
            </select>
        </div>

        <div class="entrada">
            <div class="leyenda">Vacunas al dia </div>
            <select name="vacunas-mascota${contadorMascotas + 1}" id="vacunas-mascota${contadorMascotas + 1}" required="required">
                <option value="" selected="selected">Seleccione una respuesta</option>
                <option value="0">si</option>
                <option value="1">no</option>
                <option value="2">no aplica</option>
            </select>
        </div>

        <div class="entrada">
            <div class="leyenda">Foto</div>
            <input name="foto-mascota${contadorMascotas + 1}${1}" type="file" id="foto-mascota${contadorMascotas + 1}${1}" required="required" accept="image/jpeg" >
            <button onclick="agregarOtraFoto(${contadorMascotas + 1})">
                agregar otra foto
            </button>
            <div id="entrada${contadorMascotas + 1}"></div> <!--agrega otro input para foto-->
            
        </div>
`;
    contadorMascotas = contadorMascotas + 1;
}

/**
 *Muestra ventana para preguntar si esta seguro al enviar formulario
 */
function Pregunta() {
    if (validarFormulario() === true) {
        document.getElementById('error').style.display="none";
        window.scroll(0, 0);
        document.getElementById('pregunta').style.display = "block";
    }
}

/**
 *boton vuelve al formulario
 */
function noEstoySeguro() {
    document.getElementById('pregunta').style.display = "none";
}

/**
 * Imprime error
 * @param {string|number} msg
 */
function mostrarError(msg) {
    let contenedor = document.getElementById('error');
    contenedor.innerHTML = msg;
    contenedor.style.display = 'block';
    contenedor.style.fontWeight = '800';
}

/**
 *Validacion de formulario
 */
function validarFormulario() {
    let region = document.getElementById('Region').value;
    let comuna = document.getElementById('Comuna').value;
    let calle = document.getElementById('calle').value;
    let numero = document.getElementById('numero').value;
    let sector = document.getElementById('sector').value;
    let nombre = document.getElementById('nombre').value;
    let email = document.getElementById('email').value;
    let celular = document.getElementById('celular').value;



    //let tipomascota = document.getElementById('tipo-mascota').value;
    //let edad = document.getElementById('edad-mascota').value;
    //let color = document.getElementById('color-mascota').value;
    //let raza = document.getElementById('raza-mascota').value;
    //let esterilizado = document.getElementById('esterilizado-mascota').value;
    //let vacunas = document.getElementById('vacunas-mascota').value;
    if (region ===""){
        mostrarError('Selecciona una región');
        return false;
    }
    if(comuna===""){
        mostrarError('Selecciona una comuna');
        return false;
    }
    if(calle===""){
        mostrarError('El nombre de calle es obligatorio');
        return false;
    }
    if(calle.length>250){
        mostrarError('El nombre de calle ingresado es muy largo');
        return false;
    }
    if(numero===""){
        mostrarError('El número de calle es obligatorio');
        return false;
    }
    if(numero.length>20){
        mostrarError('El número de calle ingresado es muy largo');
        return false;
    }
    if(sector.length>250){
        mostrarError('El sector ingresado es muy largo');
        return false;
    }
    if(nombre===""){
        mostrarError('El nombre de contacto es obligatorio');
        return false;
    }
    if(nombre.length>200){
        mostrarError('El nombre de contacto ingresado es muy largo');
        return false;
    }
    let regex_email=/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
    if(!regex_email.test(email)){
        mostrarError('El email ingresado no es válido');
        return false;
    }
    let regex_celular= /^(\+?56)?(\s?)(0?9)(\s?)[9876543]\d{7}$/
    if(celular!=""){
        if(!regex_celular.test(celular)){
        mostrarError('El celular ingresado no es válido');
        return false;
    }
    }

    for (var j=1;j<=contadorMascotas;j++){

        var i= j.toString();
        let classlenght=document.getElementsByClassName('foto' + i).length;//cantidad de fotos de la mascota i
        if((document.getElementById('tipo-mascota'+i).value)===""){
            mostrarError('Debes seleccionar el tipo de la mascota '+i);
            return false;
        }
        if(document.getElementById('edad-mascota'+i).value===""){
            mostrarError('Debes ingresar la edad de la mascota '+i);
            return false;
        }
        let regex_edad=/^\d+$/
        if(!regex_edad.test(document.getElementById('edad-mascota'+i).value)){
            mostrarError('la edad de la mascota '+i+' debe ser un número');
            return false;
        }
        if(document.getElementById('color-mascota'+i).value===""){
            mostrarError('Debes ingresar el color de la mascota '+i);
            return false;
        }
        if(document.getElementById('raza-mascota'+i).value===""){
            mostrarError('Debes ingresar la raza de la mascota '+i);
            return false;
        }
        if(document.getElementById('esterilizado-mascota'+i).value===""){
            mostrarError('Debes seleccionar una opción de estirilización de la mascota '+i);
            return false;
        }
        if(document.getElementById('vacunas-mascota'+i).value===""){
            mostrarError('Debes seleccionar una opción de vacunas de la mascota '+i);
            return false;
        }
        for(var x=1;x<=classlenght+1;x++)
         if(document.getElementById('foto-mascota'+i+x).value===""){
            mostrarError('Debes ingresar una foto de la mascota '+i);
            return false;
        }
    }
    return true;
}