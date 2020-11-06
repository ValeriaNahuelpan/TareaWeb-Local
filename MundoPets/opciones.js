//Creando arreglos con las comunas por region
var metropolitana = ["Colina","Lampa","Tiltil","Pirque","Puente Alto","San José de Maipo","Buin", "Calera de Tango","Paine","San Bernardo","Alhué","Curacaví","María Pinto","Melipilla",
"San Pedro","Cerrillos","Cerro Navia","Conchalí","El Bosque","Estación Central","Huechuraba","Independencia","La Cisterna","La Granja","La Florida","La Pintana","La Reina","Las Condes",
"Lo Barnechea","Lo Espejo","Lo Prado","Macul","Maipú","Ñuñoa","Pedro Aguirre Cerda","Peñalolen","Providencia","Pudahuel","Quilicura","Quinta Normal","Recoleta", "Renca","San Miguel",
"San Joaquín","San Ramón","Santiago","Vitacura","El Monte","Isla de Maipo","Padre Hurtado","Peñaflor","Talagante"];

var aricaParinacota = ["Arica","Camarones","General Lagos","Putre"];

var tarapaca = ["Alto Hospicio","Iquique","Camiña","Colchane","Huara","Pica","Pozo Almonte"];

var antofagasta = ["Antofagasta","Mejillones","Sierra Gorda","Taltal","Calama","Ollagüe","San Pedro de Atacama","María Elena", "Tocopilla"];

var atacama = ["Chañaral","Diego de Almagro","Caldera","Copiapo","Tierra Amarilla","Alto del Carmen","Freirina","Huasco","Vallenar"];

var coquimbo = ["Canela","Illapel","Los Vilos","Salamanca","Andacollo","Coquimbo","La Higuera","La Serena","Paihuano","Vicuña","Combarbalá","Monte Patria","Ovalle","Punitaqui","Río Hurtado"];

var valparaiso = ["Isla de Pascua","Calle Larga","Los Andes","Rinconada de los Andes","San Esteban","Limache","Olmué","Quilpué","Villa Alemana","Cabildo","La Ligua","Papudo","Petorca",
                "Zapallar","Hijuelas","La Calera","La Cruz","Nogales","Quillota","Algarrobo","Cartagena","El Quisco","El Tabo","San Antonio","Santo Domingo","Catemu","Llaillay","Panquehue",
                "Putaendo","San Felipe","Santa María","Casablanca","Concón","Juán Fernández","Puchuncavi","Quintero","Valparaíso","Viña del Mar"];

var libertadorBernardoOhiggins = ["Codegua","Coínco","Coltauco","Doñihue","Graneros","Las Cabras","Machalí","Malloa","Olivar","Peumo","Pichidegua","Quinta de Tilcoco","Rancagua","Requínoa",
                                "Rengo","San Francisco de Mostazal","San Vicente de Tagua Tagua","La Estrella","Litueche","Marchigüe","Navidad","Paredones","Pichilemu","Chépica","Chimbarongo",
                                "Lolol","Nancagua","Palmilla","Peralillo","Placilla","Pumanque","San Fernando","Santa Cruz"];

var maule = ["Cauquenes","Chanco","Pelluhue","Curicó","Hualañé","Licantén","Molina","Rauco","Romeral","Sagrada Familia","Teno","Vichuquén","Colbún","Linares","Longaví","Parral","Retiro",
            "San Javier de Loncomilla","Villa Alegre","Yerbas Buenas","Constitución","Curepto","Empedrado","Maule","Pelarco","Pencahue","Río Claro","San Clemente","San Rafael","Talca"];

var ñuble = ["Bulnes","Chillán","Chillán Viejo","El Carmen","Pemuco","Pinto","Quillón","San Ignacio","Yungay","Cobquecura","Coelemu","Ninhue","Portezuelo","Quirihue","Ránquil","Treguaco",
            "Coihueco","Ñiquén","San Carlos","San Fabián","San Nicolás"];

var biobio = ["Arauco","Cañete","Contulmo","Curanilahue","Lebu","Los Álamos","Tirúa","Alto BioBío","Antuco","Cabrero","Laja","Los Ángeles","Mulchén","Nacimiento","Negrete","Quilaco",
            "Quilleco","San Rosendo","Santa Bárbara","Tucapél","Yumbel","Chiguayante","Concepción","Coronel","Florida","Hualpén","Hualqui","Lota","Penco","San Pedro de la Paz","Santa Juana",
            "Talcahuano","Tomé"];

var araucania = ["Carahue","Cholchol","Cunco","Curarrehue","Freire","Galvarino","Gorbea","Lautaro","Loncoche","Melipeuco","Nueva Imperial","Padre Las Casas","Perquenco","Pitrufquén",
                "Pucón","Saavedra","Temuco","Teodoro Schmidt","Toltén","Vilcún","Villarica","Angol","Collipulli","Curacautín","Ercilla","Lonquimay","Los Sauces","Lumaco","Purén","Renaico",
                "Traiguén","Victoria"];

var losrios = ["Futrono","La Unión","Lago Ranco","Río Bueno","Corral","Lanco","Los Lagos","Máfil","Mariquina","Paillaco","Panguipulli","Valdivia"];

var loslagos = ["Ancud","Castro","Chonchi","Curaco de Vélez","Dalcahue","Puqueldón","Queilén","Quellón","Quemchi","Quinchao","Calbuco","Cochamó","Fresia","Fresia","Frutillar","Llanquihue",
                "Los Muermos","Maullín","Puerto Montt","Puerto Varas","Osorno","Puerto Octay","Purranque","Puyehue","Río Negro","San Pablo","San Juan de la Costa","Chaitén","Futaleufú",
                "Hualaihué","Palena"];

var aysen = ["Aysén","Cisnes","Guaitecas","Cochrane","O'Higgins","Tortel","Coyhaique","Lago Verde","Chile Chico","Río Ibáñez"];

var magallanesAntartica = ["Antártica","Cabo de Hornos","Laguna Blanca","Punta Arenas","Río Verde","San Gregorio","Porvenir","Primavera","Timaukel","Natales","Torres del Paine"];

function cambiarComuna(){

    switch(document.getElementById("Region").value){
        case "Metropolitana de Santiago":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < metropolitana.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = metropolitana[i];
                opt.value = metropolitana[i];
                sel.appendChild(opt);
            }
            break;
        case "Arica y Parinacota":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < aricaParinacota.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = aricaParinacota[i];
                opt.value = aricaParinacota[i];
                sel.appendChild(opt);
            }
            break;
        case "Tarapacá":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < tarapaca.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = tarapaca[i];
                opt.value = tarapaca[i];
                sel.appendChild(opt);
            }
            break;
        case "Antofagasta":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < antofagasta.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = antofagasta[i];
                opt.value = antofagasta[i];
                sel.appendChild(opt);
            }
            break;
        case "Atacama":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < atacama.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = atacama[i];
                opt.value = atacama[i];
                sel.appendChild(opt);
            }
            break;
        case "Coquimbo":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < coquimbo.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = coquimbo[i];
                opt.value = coquimbo[i];
                sel.appendChild(opt);
            }
            break;
        case "Valparaíso":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < valparaiso.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = valparaiso[i];
                opt.value = valparaiso[i];
                sel.appendChild(opt);
            }
            break;
        case "Libertador G. Bernardo O'Higgins":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < libertadorBernardoOhiggins.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = libertadorBernardoOhiggins[i];
                opt.value = libertadorBernardoOhiggins[i];
                sel.appendChild(opt);
            }
            break;
        case "Maule":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < maule.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = maule[i];
                opt.value = maule[i];
                sel.appendChild(opt);
            }
            break;
        case "Ñuble":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < ñuble.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = ñuble[i];
                opt.value = ñuble[i];
                sel.appendChild(opt);
            }
            break;
        case "Biobío":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < biobio.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = biobio[i];
                opt.value = biobio[i];
                sel.appendChild(opt);
            }
            break;
        case "Araucanía":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < araucania.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = araucania[i];
                opt.value = araucania[i];
                sel.appendChild(opt);
            }
            break;
        case "Los Ríos":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < losrios.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = losrios[i];
                opt.value = losrios[i];
                sel.appendChild(opt);
            }
            break;
        case "Los Lagos":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < loslagos.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = loslagos[i];
                opt.value = loslagos[i];
                sel.appendChild(opt);
            }
            break;
        case "Aysén del G. Carlos Ibañez del Campo":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < aysen.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = aysen[i];
                opt.value = aysen[i];
                sel.appendChild(opt);
            }
            break;
        case "Magallanes y la Antártica Chilena":
            document.getElementById("Comuna").options.length = 1;
            var sel = document.getElementById("Comuna");
            for(var i = 0; i < magallanesAntartica.length; i++) {
                var opt = document.createElement('option');
                opt.innerHTML = magallanesAntartica[i];
                opt.value = magallanesAntartica[i];
                sel.appendChild(opt);
            }
            break;
    }
}