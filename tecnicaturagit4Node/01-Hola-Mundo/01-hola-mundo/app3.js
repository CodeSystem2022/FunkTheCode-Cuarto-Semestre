console.log("inicio del programa");
setTimeout(()=>{
    console.log("primer Timeout");
}, 3000);

setTimeout(()=>{
    console.log("segundo Timeout");
}, 0);

setTimeout(()=>{
    console.log("tercero Timeout");
}, 0);

console.log("fin del programa");