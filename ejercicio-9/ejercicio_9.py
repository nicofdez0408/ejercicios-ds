class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se han ingresado {monto}. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, monto):
        if monto > 0:
            if self.saldo - monto < 0:
                print("Saldo insuficiente para realizar la operacion")
            else:
                self.saldo -= monto
                print(f"Se han retirado {monto}. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a retirar debe ser positiva.")
            
    def mostrar_info(self):
            print(f"Titular: {self.titular} | Saldo: {self.saldo}")
            
def main():
    cuenta = CuentaBancaria("Juan Perez", 1000.0)
    cuenta.mostrar_info()
    
    cuenta.depositar(500.0)
    cuenta.retirar(200.0)
    cuenta.retirar(1500.0)  # Intento de retirar más de lo disponible
    cuenta.depositar(-100.0)  # Intento de depositar una cantidad negativa
    cuenta.retirar(-50.0)  # Intento de retirar una cantidad negativa
    
    cuenta.mostrar_info()
    
    cuenta2 = CuentaBancaria("Maria Lopez")
    cuenta2.mostrar_info()
    cuenta2.depositar(300.0)
    cuenta2.retirar(100.0)
    cuenta2.mostrar_info()
    
if __name__ == "__main__":
    main()