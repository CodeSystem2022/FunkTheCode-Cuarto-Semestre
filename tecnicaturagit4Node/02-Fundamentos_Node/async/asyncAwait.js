// la palabra async no es necesaria en las funciones , por que ya son asincronas
//igual proyectan una sincronia visual
async function hola(nombre){
    return new Promise(function(resolve, reject){
        setTimeout(function(){
            console.log("Hola " +nombre);
            resolve(nombre);
        }, 1000);
    });
    
}

async function hablar(nombre){
    return new Promise((resolve, reject)=>{ // usamos la sintaxis es6
        setTimeout(function(){
            console.log("bla bla bla bla");
            resolve(nombre);
        }, 1000);
    });
}

async function adios(nombre){
    return new Promise((resolve, reject)=>{
        setTimeout(function(){
            console.log("Adios "+ nombre);
            //resolve();
            reject("hay un error");
        }, 1000);  
    })
    
}

//await hola("Ariel"); // esto es una mala sintaxis
//await solo es valido dentro de una funcion asincrona
async function main(){
    let nombre = await hola("Ariel");
    await hablar();
    await hablar();
    await hablar();
    await adios(nombre);
    console.log("termino  el proceso...")
}

console.log("Empezamos el proceso...")
main();
console.log("esta va a ser la segunda instruccion");
