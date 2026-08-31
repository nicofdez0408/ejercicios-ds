const formulario = document.getElementById("formularioContacto");
const inputNombre = document.getElementById("nombre");
const inputEmail = document.getElementById("email");

const errorNombre = document.getElementById("errorNombre");
const errorEmail = document.getElementById("errorEmail");
const mensajeExito = document.getElementById("mensajeExito");

function validarFormulario(evento) {

    evento.preventDefault();

    const nombre = inputNombre.value.trim();
    const correo = inputEmail.value.trim();
    let esValido = true;

    errorNombre.style.display = "none";
    errorEmail.style.display = "none";
    mensajeExito.style.display = "none";

    if (nombre === "") {
        errorNombre.style.display = "block";
        esValido = false;
    }

    if (correo === "") {
        errorEmail.style.display = "block";
        esValido = false;
    }

    if (esValido) {
        mensajeExito.style.display = "block";
        inputNombre.value = "";
        inputEmail.value = "";
    }
}

formulario.addEventListener("submit", validarFormulario);