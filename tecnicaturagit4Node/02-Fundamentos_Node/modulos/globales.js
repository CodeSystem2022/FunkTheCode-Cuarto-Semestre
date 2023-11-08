//this === global = true

//mostrar algo en consola
//console.log();

//mostrar un mensaje en forma de error
//console.error();

//ejecutar un coodigo despues de un intervalo de tiempo
//setTimeout(()=>{});

//ejecutar un codigo cada intervalo de tiempo
//setInterval(()=>{});

//da prioridad de ejecucion a una funcion asincronica
//setImmdiate(()=>{});

//console.log(setInterval);

let i = 0;
let intervalo = setInterval(()=>{
    console.log("hola");
    if ( i === 3){
        clearInterval(intervalo); // detenemos la funcion
   }
    i++;
}, 1000);

setImmediate(()=>{
    console.log("saludo inmediato");
})

//require();

console.log(__filename);

globalThis.miVariable = "mi variable global";
console.log(miVariable);