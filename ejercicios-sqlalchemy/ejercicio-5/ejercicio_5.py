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
    
    clases: Mapped[List["Clase"]] = relationship(back_populates="curso")
    
class Clase(Base):
    __tablename__ = "clases"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(100))
    duracion_minutos: Mapped[int] = mapped_column()
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped["Curso"] = relationship(back_populates="clases")
    
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
                        Curso(
                            titulo="Introducción a Python", 
                            creditos=3,
                            clases=[
                                Clase(tema="Variables y Tipos de Datos", duracion_minutos=90),
                                Clase(tema="Estructuras de Control", duracion_minutos=120)
                            ]
                        )
                    ])
            ]
        )
        session.add(depto_sistemas)
        session.commit()
        print("-> Datos guardados exitosamente.\n")
    
    with Session(engine) as session:
        stmt = select(Curso).where(Curso.titulo == "Introducción a Python")
        curso = session.scalars(stmt).first()
        
        if curso:
            print(f"Curso encontrado: {curso.titulo}")
            print("Lista de clases:")
            for clase in curso.clases:
                print(f" - Tema: {clase.tema} | Duración: {clase.duracion_minutos} min")
                
if __name__ == "__main__":
    main()