def contiene_mayuscula(contrasenia):
    for letra in contrasenia:
        if letra.isupper():
            return True
    return False

def contiene_minuscula(contrasenia):
    for letra in contrasenia:
        if letra.islower():
            return True
    return False

def evaluar_contrasenia(contrasenia):
    return contiene_mayuscula(contrasenia) and contiene_minuscula(contrasenia) and len(contrasenia) >= 8

def main():
    contrasenia = input("Ingrese una contraseña: ")
    if evaluar_contrasenia(contrasenia):
        print("La contraseña es segura.")
    else:
        print("La contraseña no es segura. Debe contener al menos una letra mayúscula, una letra minúscula y tener al menos 8 caracteres.")
        
if __name__ == "__main__":
    main()