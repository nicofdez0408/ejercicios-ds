def sumar_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

def buscar_divisibles_por_3(inicio, fin):
    divisibles = []
    for i in range(inicio, fin + 1):
        if i % 3 == 0:
            divisibles.append(i)
    return divisibles

def menu_interactivo():
    while True:
        print("Menú Interactivo:")
        print("a. Calcular la suma de los primeros N números naturales")
        print("b. Encontrar números divisibles por 3 en un rango")
        print("c. Salir")
        
        opcion = input("Seleccione una opción: ").strip().lower()
        
        match opcion:
            case "a":
                n = int(input("Ingrese la cantidad de números naturales a sumar: "))
                resultado = sumar_naturales(n)
                print(f"La suma de los primeros {n} números naturales es: {resultado}")
            case "b":
                inicio = int(input("Ingrese el valor inicia del rango: "))
                fin = int(input("Ingrese el valor final del rango: "))
                resultado = buscar_divisibles_por_3(inicio, fin)
                print(f"Los números divisibles por 3 en el rango [{inicio}, {fin}] son: {resultado}")
            case "c":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

def main():
    menu_interactivo()
    
if __name__ == "__main__":
    main()