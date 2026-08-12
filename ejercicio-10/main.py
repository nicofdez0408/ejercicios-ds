from biblioteca.modelos.libro import Libro
import biblioteca.servicios.prestamo as prestamo

def main():
    print("=== SISTEMA DE GESTIÓN DE BIBLIOTECA ===\n")
    libro = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0156012195")
    print(prestamo.consultar_disponibilidad(libro))
    print(prestamo.realizar_prestamo(libro))
    print(prestamo.consultar_disponibilidad(libro))
    
    print(prestamo.realizar_prestamo(libro))  # Intento de préstamo cuando el libro ya está prestado
    
    print(prestamo.realizar_devolucion(libro))
    print(prestamo.consultar_disponibilidad(libro))
    
    print(prestamo.realizar_devolucion(libro))  # Intento de devolución cuando el libro ya está disponible
    
if __name__ == "__main__":
    main()
    