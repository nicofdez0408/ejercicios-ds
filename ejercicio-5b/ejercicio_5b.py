PASSWD_CORRECTA = "Admin1234"

def inicio_sesion():
    intentos = 0
    while intentos < 3:
        contrasenia = input("Ingrese la contraseña: ")
        if contrasenia == PASSWD_CORRECTA:
            print("Inicio de sesión exitoso!")
            return
        else:
            print("Contraseña incorrecta. Intente nuevamente.")
            intentos += 1
    print("Cuenta bloqueada. Ha excedido el número máximo de intentos.")
    
def main():
    inicio_sesion()
    
if __name__ == "__main__":
    main()