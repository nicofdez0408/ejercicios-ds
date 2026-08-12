from pydantic import BaseModel, Field, ValidationError
from typing import Annotated, Optional

CoordenadaGPS = Annotated[float, Field(ge=-90.0, le=90.0, description="La coordenada GPS debe estar entre -90 y 90 grados")]

class Ubicacion(BaseModel):
    latitud: CoordenadaGPS
    longitud: CoordenadaGPS
    etiqueta: Optional[str] = Field(default=None, description="Etiqueta opcional para la ubicación")
    
def main():
    # 1. Error de latitud (mayor a 90.0)
    try:
        Ubicacion(latitud=91.0, longitud=45.0)
    except ValidationError as error:
        print(error, "\n")
        
    # 2. Error de longitud (menor a -90.0)
    try:
        Ubicacion(latitud=45.0, longitud=-91.0)
    except ValidationError as error:
        print(error, "\n")
        
    # 3. Instancia válida con etiqueta
    ubicacion_ok = Ubicacion(latitud=40.7128, longitud=-74.0060, etiqueta="Nueva York")
    print("Éxito! Ubicación creada con etiqueta:")
    print(ubicacion_ok, "\n")
    
    # 4. Instancia válida sin etiqueta
    ubicacion_ok_sin_etiqueta = Ubicacion(latitud=34.0522, longitud=-58.3815)
    print("Éxito! Ubicación creada sin etiqueta:")
    print(ubicacion_ok_sin_etiqueta)
    
if __name__ == "__main__":
    main()