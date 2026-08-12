from pydantic import BaseModel, EmailStr, Field, ValidationError

class Estudiante(BaseModel):
    legajo: int = Field(gt = 0, description = "El legajo debe ser un número entero positivo")
    nombre_completo: str = Field(min_length = 5, description = "El nombre completo debe tener al menos 5 caracteres")
    email: EmailStr
    promedio: float = Field(ge = 0.0, le = 10.0, default = 0.0, description = "El promedio debe estar entre 0 y 10")
    
def main():
    
    # 1. Error de Legajo (menor o igual a 0)
    try:
        Estudiante(legajo=0, nombre_completo="Juan Perez", email="juan@mail.com")
    except ValidationError as error:
        print(error, "\n")
        
    # 2. Error de Nombre Completo (menos de 5 caracteres)
    try:
        Estudiante(legajo=10, nombre_completo="Ana", email="ana@mail.com")
    except ValidationError as error:
        print(error, "\n")
        
    # 3. Error de Email (formato incorrecto sin el @ ni dominio)
    try:
        Estudiante(legajo=15, nombre_completo="Pedro Gomez", email="correo_falso.com")
    except ValidationError as error:
        print(error, "\n")
        
    # 4. Error de Promedio (mayor a 10.0)
    try:
        Estudiante(legajo=20, nombre_completo="Maria Silva", email="maria@mail.com", promedio=11.5)
    except ValidationError as error:
        print(error, "\n")

    # 5. Instancia válida
    estudiante_ok = Estudiante(
        legajo=999, 
        nombre_completo="Lionel Messi", 
        email="lio@campeones.com", 
        promedio=9.5
    )
    print("Éxito! Estudiante creado:")
    print(estudiante_ok)

if __name__ == "__main__":
    main()