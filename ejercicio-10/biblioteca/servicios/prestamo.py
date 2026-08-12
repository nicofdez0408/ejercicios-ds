import biblioteca.modelos.libro as libro

def realizar_prestamo(libro):
    if libro.disponible:
        libro.disponible = False
        return f"El libro '{libro.titulo}' ha sido prestado."
    else:
        return f"El libro '{libro.titulo}' no está disponible para préstamo."
    
def realizar_devolucion(libro):
    if not libro.disponible:
        libro.disponible = True
        return f"El libro '{libro.titulo}' ha sido devuelto."
    else:
        return f"El libro '{libro.titulo}' no estaba prestado."
    
def consultar_disponibilidad(libro):
    if libro.disponible:
        return f"El libro '{libro.titulo}' está disponible para préstamo."
    else:
        return f"El libro '{libro.titulo}' no está disponible para préstamo."



