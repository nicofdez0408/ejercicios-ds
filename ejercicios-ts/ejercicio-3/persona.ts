interface Persona {
    nombre: string
    edad: number
}

const estudiante: Persona = {
    nombre: "Juan",
    edad: 22
};

console.log("Datos del estudiante:");
console.log(`Nombre: ${estudiante.nombre}`);
console.log(`Edad: ${estudiante.edad}`)