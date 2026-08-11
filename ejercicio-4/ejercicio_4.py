def convertir_a_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def convertir_a_fahrenheit(celcius):
    return (celcius * 9 / 5) + 32

def main():
    temperatura = float(input("Ingrese la temperatura: "))
    unidad = input("Ingrese la escala original (C para Celsius, F para Fahrenheit): ").upper()

    if unidad == "C":
        resultado = convertir_a_fahrenheit(temperatura)
        print(f"{temperatura}°C son {resultado:.2f}°F")
    elif unidad == "F":
        resultado = convertir_a_celcius(temperatura)
        print(f"{temperatura}°F son {resultado:.2f}°C")
    else:
        print("Escala no válida. Por favor ingrese C o F.")
        
if __name__ == "__main__":
    main()