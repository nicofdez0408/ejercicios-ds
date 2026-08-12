from pydantic import BaseModel, Field, ValidationError
from typing import Optional

class PerfilUsuario(BaseModel):
    username: str = Field(pattern=r"^[a-z0-9_]{3,20}$")
    biografia: Optional[str] = Field(default=None, max_length=200)
    redes_sociales: Optional[list[str]] = Field(default=None)
    
def main():
    # 1. Error de username (no cumple con el patrón)
    try:
        PerfilUsuario(username="InvalidUsername!", biografia="Esta es una biografía válida.", redes_sociales=["https://twitter.com/usuario"])
    except ValidationError as error:
        print(error, "\n")
        
    # 2. Error de biografía (excede los 200 caracteres)
    try:
        PerfilUsuario(username="usuario_valido", biografia="A" * 201, redes_sociales=["https://twitter.com/usuario"])
    except ValidationError as error:
        print(error, "\n")
        
    # 3. Instancia válida
    perfil_ok = PerfilUsuario(
        username="usuario_valido", 
        biografia="Esta es una biografía válida.", 
        redes_sociales=["https://twitter.com/usuario"])
    print("Éxito! Perfil de usuario creado:")
    print(perfil_ok)

if __name__ == "__main__": 
    main()