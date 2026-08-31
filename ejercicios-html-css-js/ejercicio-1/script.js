const boton = document.getElementById('btnColor');

boton.addEventListener('click', function() {
    const colorAleatorio = '#' + Math.floor(Math.random()*16777215).toString(16);
    document.body.style.backgroundColor = colorAleatorio;
});