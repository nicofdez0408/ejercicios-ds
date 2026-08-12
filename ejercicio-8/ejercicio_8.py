def calcular_descuento(precio_base, porcentaje_descuento):
    descuento = precio_base * (porcentaje_descuento / 100)
    return precio_base - descuento

def calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip=False):
    if precio_base < 0 or porcentaje_descuento < 0:
        raise ValueError("El precio base y el porcentaje de descuento deben ser positivos.")
    
    precio_rebajado = calcular_descuento(precio_base, porcentaje_descuento)
    
    if es_vip:
        precio_rebajado -= (precio_rebajado * 0.05)
    
    return precio_rebajado

def main():
    print("--- Pruebas del calculador de precios ---")
    
    # Prueba 1: Usando los valores por defecto (10% descuento, no VIP)
    res1 = calcular_precio_final(1000)
    print(f"Prueba 1 (Base 1000, por defecto): ${res1:.2f}")
    
    # Prueba 2: Modificando el descuento (20% descuento, no VIP)
    res2 = calcular_precio_final(1000, 20)
    print(f"Prueba 2 (Base 1000, 20% desc, no VIP): ${res2:.2f}")
    
    # Prueba 3: Cliente VIP, pero con el descuento base por defecto (10%)
    res3 = calcular_precio_final(1000, es_vip=True)
    print(f"Prueba 3 (Base 1000, 10% desc, VIP): ${res3:.2f}")
    
    # Prueba 4: Todo personalizado (30% descuento, VIP)
    res4 = calcular_precio_final(1000, 30, True)
    print(f"Prueba 4 (Base 1000, 30% desc, VIP): ${res4:.2f}")
    
    # Prueba 5: Forzando el error para ver si la validación funciona
    print("\n--- Prueba de Validación de Error ---")
    try:
        print("Intentando calcular con un precio negativo (-500)...")
        calcular_precio_final(-500)
    except ValueError as e:
        print(f"Excepción capturada con éxito!: {e}")

if __name__ == "__main__":
    main()