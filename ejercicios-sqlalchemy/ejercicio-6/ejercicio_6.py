from database import Base, engine
from typing import List
from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, DateTime, Table, select
from sqlalchemy.orm import Mapped, mapped_column, Session, relationship

inscripcion = Table(
    "inscripciones",
    Base.metadata,
    Column("estudiante_id", ForeignKey("estudiantes.id"), primary_key=True),
    Column("curso_id", ForeignKey("cursos.id"), primary_key=True)
)

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
    
    estudiantes: Mapped[List["Estudiante"]] = relationship(secondary=inscripcion, back_populates="cursos")
    
class Clase(Base):
    __tablename__ = "clases"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(100))
    duracion_minutos: Mapped[int] = mapped_column()
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped["Curso"] = relationship(back_populates="clases")
    
class Estudiante(Base):
    __tablename__ = "estudiantes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    legajo: Mapped[str] = mapped_column(String(20))
    
    cursos: Mapped[List["Curso"]] = relationship(secondary=inscripcion, back_populates="estudiantes")


    
def main():
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        depto = Departamento(nombre="Sistemas")
        profe = Profesor(nombre="Carlos Ruiz", email="carlos@u.edu", departamento=depto)
        
        curso_python = Curso(titulo="Introducción a Python", creditos=3, profesor=profe)
        curso_bd = Curso(titulo="Bases de Datos", creditos=4, profesor=profe)
        
        estudiante_1 = Estudiante(nombre="Nicolás", legajo="LEG-001")
        estudiante_2 = Estudiante(nombre="Martina", legajo="LEG-002")
        
        estudiante_1.cursos.append(curso_python)
        estudiante_1.cursos.append(curso_bd)
        
        estudiante_2.cursos.append(curso_bd)
        
        session.add_all([estudiante_1, estudiante_2])
        session.commit()
        print("-> Estudiantes, Cursos e Inscripciones guardadas exitosamente.\n")
    
    with Session(engine) as session:
        stmt = select(Curso).where(Curso.titulo == "Bases de Datos")
        curso = session.scalars(stmt).first()
        
        if curso:
            print(f"Alumnos inscritos en el curso '{curso.titulo}':")
            for estudiante in curso.estudiantes:
                print(f" - {estudiante.nombre} (Legajo: {estudiante.legajo})")
                
        print("\n----------------------\n")
        stmt_est = select(Estudiante).where(Estudiante.nombre == "Nicolás")
        nico = session.scalars(stmt_est).first()
        
        if nico:
            print(f"Cursos en los que está anotado {nico.nombre}:")
            for c in nico.cursos:
                print(f" - {c.titulo}")
                
if __name__ == "__main__":
    main()