from database import Base, engine
from typing import List
from datetime import datetime
from sqlalchemy import ForeignKey, String, DateTime, select
from sqlalchemy.orm import Mapped, mapped_column, Session, relationship

class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))

    profesores: Mapped[List["Profesor"]] = relationship()
    
class Profesor(Base):
    __tablename__ = "profesores"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))
    
def main():
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        
        depto_sistemas = Departamento(
            nombre="Sistemas",
            profesores=[
                Profesor(nombre="Carlos Ruiz", email="carlos@u.edu"),
                Profesor(nombre="Lucía Gómez", email="lucia@u.edu")
            ]
        )
        session.add(depto_sistemas)
        session.commit()
        print("-> Departamento y Profesores guardados exitosamente.\n")
    
    with Session(engine) as session:
        
        stmt = select(Departamento).where(Departamento.nombre == "Sistemas")
        depto = session.scalars(stmt).first()
        
        if depto:
            print(f"Departamento: {depto.nombre}")
            print("Lista de profesores (obtenida mediante la relación):")
            for prof in depto.profesores:
                print(f" - {prof.nombre} | {prof.email}")
                
if __name__ == "__main__":
    main()