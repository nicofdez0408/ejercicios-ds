from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import Union, Literal

class Dispositivo(BaseModel):
    id_dispositivo: Union[int, str]
    tipo: Literal["sensor", "actuador", "gateway"]
    
def main():
    # 1. Error de tipo de dispositivo (no es "sensor", "actuador" ni "gateway")
    try:
        Dispositivo(id_dispositivo=1, tipo="otro")
    except ValidationError as error:
        print(error, "\n")
        
    # 2. Instancia válida con id_dispositivo como int
    dispositivo_ok_int = Dispositivo(id_dispositivo=123, tipo="sensor")
    print("Éxito! Dispositivo creado con id_dispositivo como int:")
    print(dispositivo_ok_int, "\n")
    
    # 3. Instancia válida con id_dispositivo como str
    dispositivo_ok_str = Dispositivo(id_dispositivo="abc123", tipo="actuador")
    print("Éxito! Dispositivo creado con id_dispositivo como str:")
    print(dispositivo_ok_str)
    
if __name__ == "__main__":
    main()