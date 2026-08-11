def calcular_costo_total(pasaje, alojamiento, noches):
    return pasaje + (alojamiento * noches)

def evaluar_presupuesto(costo_total, dinero_disponible):
    return dinero_disponible >= costo_total

def main():
    costo_pasaje = float(input("Ingrese el costo del pasaje: "))
    costo_alojamiento = float(input("Ingrese el costo del alojamiento por noche: "))
    noches = int(input("Ingrese la cantidad de noches: "))
    dinero_disponible = float(input("Ingrese la cantidad de dinero disponible: "))
    
    costo_total = calcular_costo_total(costo_pasaje, costo_alojamiento, noches)
    es_suficiente = evaluar_presupuesto(costo_total, dinero_disponible)
    
    print("\n--- Resumen del Viaje ---")
    print(f"Costo total calculado: ${costo_total}")
    print(f"Dinero disponible: ${dinero_disponible}")
    print(f"El dinero es suficiente?: {es_suficiente}")
    
if __name__ == "__main__":
    main()