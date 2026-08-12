from pydantic import BaseModel, EmailStr, Field, ValidationError

class UsuarioSistema(BaseModel):
    email: EmailStr
    nivel_accesso: int = Field(ge=1, le=5, description="El nivel de acceso debe estar entre 1 y 5")
    
def main():
    try:
        usuario = UsuarioSistema(email="estoesinvalido", nivel_accesso=7)
    except ValidationError as error:
        print(error, "\n")

if __name__ == "__main__":
    main()
    
