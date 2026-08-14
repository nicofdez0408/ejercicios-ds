from database import Base, engine
from typing import List
from datetime import datetime
from sqlalchemy import ForeignKey, String, DateTime, select
from sqlalchemy.orm import Mapped, mapped_column, Session, relationship

class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))

    profesores: Mapped[List["Profesor"]] = relationship(back_populates="departamento")
    
class Profesor(Base):
    __tablename__ = "profesores"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))
    
    departamento: Mapped["Departamento"] = relationship(back_populates="profesores")
    
    cursos: Mapped[List["Curso"]] = relationship(back_populates="profesor")
    
class Curso(Base):
    __tablename__ = "cursos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column()
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    profesor: Mapped["Profesor"] = relationship(back_populates="cursos")    
    
def main():
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        
        depto_sistemas = Departamento(
            nombre="Sistemas",
            profesores=[
                Profesor(
                    nombre="Carlos Ruiz", 
                    email="carlos@u.edu", 
                    cursos=[
                        Curso(titulo="Introducción a Python", creditos=3),
                        Curso(titulo="Estructuras de Datos", creditos=4)
                    ])
            ]
        )
        session.add(depto_sistemas)
        session.commit()
        print("-> Departamento, profesor y cursos guardados exitosamente.\n")
    
    with Session(engine) as session:
        
        stmt = select(Profesor).where(Profesor.nombre == "Carlos Ruiz")
        profesor = session.scalars(stmt).first()
        
        if profesor:
            print(f"Profesor: {profesor.nombre}")
            print(f"Departamento al que pertenece: {profesor.departamento.nombre}")
            print("Cursos dictados:")
            for curso in profesor.cursos:
                print(f" - {curso.titulo} ({curso.creditos} créditos)")
                
if __name__ == "__main__":
    main()