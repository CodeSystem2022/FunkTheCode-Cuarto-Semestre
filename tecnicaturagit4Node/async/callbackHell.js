function hola(nombre, miCallback){
    setTimeout(function(){
        console.log("Hola " +nombre);
        miCallback(nombre);
    }, 1000);
}

function hablar(miCallbackHablar){
    setTimeout(function(){
        console.log("bla bla bla bla");
        miCallbackHablar();
    }, 1000);
}

function adios(nombre, otroCallback){
    setTimeout(function(){
        console.log("Adios "+ nombre);
        otroCallback();
    }, 1500);
}


//funcion recursiva
function conversacion(nombre, veces, callback){
    if(veces > 0){
        hablar(function(){
            conversacion(nombre, --veces, callback);
        })
    } else {
        callback(nombre, callback);
    }
    
}

//--Porceso principal
console.log("iniciando el proceso...");
hola("Ariel", function(nombre){
    conversacion(nombre, 4, function(){
        console.log("terminando el proceso..."); 
    });
});
//hola("Carlos", function(nombre){
//   hablar(function(nombre){
//        hablar(function(){
//            hablar(function(){
//                hablar(function(){
//                    adios("carlos",function(){
//                        console.log("terminando el proceso...");
//                    }); 
//                });    
//            });
//        });
//    });
//});
    
