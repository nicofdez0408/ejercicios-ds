def analizar_temperaturas(registros):
    temp_min = min(registros)
    temp_max = max(registros)
    temp_promedio = sum(registros) / len(registros)
    return (temp_max, temp_min, temp_promedio)

def main():
    temperaturas_semana = [15.5, 18.2, 21.0, 14.3, 19.8, 22.1, 16.5]
    max_temp, min_temp, promedio_temp = analizar_temperaturas(temperaturas_semana)
    print("--- Análisis de Temperaturas ---")
    print(f"Registros evaluados: {temperaturas_semana}")
    print(f"Temperatura Máxima:  {max_temp} °C")
    print(f"Temperatura Mínima:  {min_temp} °C")
    print(f"Temperatura Promedio: {promedio_temp:.2f} °C")
    
if __name__ == "__main__":
    main()