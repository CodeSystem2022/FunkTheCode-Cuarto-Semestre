class Persona{
    static contadorPersonas = 0;

    constructor(nombre, apellido, edad){
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    get idPersona(){
        return this._idPersona;
    }

    get nombre(){
        this.nombre;
    }

    set nombre(nombre){
        this.nombre;
    }

    get apellido(){
        this.apellido;
    }

    set apellido(apellido){
        this.apellido;
    }

    get edad(){
        this.edad;
    }

    set edad(edad){
        this.edad;
    }

    toString(){
        return `
        ${this._idPersona}
        ${this._nombre}
        ${this._apellido}
        ${this._edad}`;
    }
    
}