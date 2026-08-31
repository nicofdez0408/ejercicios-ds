const inputTarea = document.getElementById("nuevaTarea");
const btnAgregar = document.getElementById("btnAgregar");
const listaTareas = document.getElementById("listaTareas");

function agregarTarea() {
    const texto = inputTarea.value.trim();
    
    if (texto !== "") {
        const li = document.createElement("li");
        li.textContent = texto;
        
        li.addEventListener("click", eliminarTarea);
        
        listaTareas.appendChild(li);
        inputTarea.value = "";
    }
}

function eliminarTarea() {
    this.remove(); 
}

btnAgregar.addEventListener("click", agregarTarea);