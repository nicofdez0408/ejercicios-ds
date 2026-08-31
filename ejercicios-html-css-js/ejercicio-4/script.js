
const btnRestar = document.getElementById("btnRestar")
const valorContador = document.getElementById("valorContador")
const btnSumar = document.getElementById("btnSumar")

let contador = 0;

function actualizarPantalla() {
    valorContador.textContent = contador;
}

function incrementar() {
    contador++;
    actualizarPantalla();
}

function decrementar() {
    contador--;
    actualizarPantalla();
}

btnSumar.addEventListener("click", incrementar);
btnRestar.addEventListener("click", decrementar);
