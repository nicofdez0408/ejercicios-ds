from database import Base, engine
from typing import List, Optional
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
    
    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="curso")
    
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
    
    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="estudiante")

class Inscripcion(Base):
    __tablename__ = "inscripciones"
    
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), primary_key=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"), primary_key=True)
    
    fecha_inscripcion: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    calificacion_final: Mapped[Optional[float]] = mapped_column()
    
    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")

    
def main():
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        depto = Departamento(nombre="Sistemas")
        profe = Profesor(nombre="Carlos Ruiz", email="carlos@u.edu", departamento=depto)
        
        curso_python = Curso(titulo="Introducción a Python", creditos=3, profesor=profe)
        curso_bd = Curso(titulo="Bases de Datos", creditos=4, profesor=profe)
        
        estudiante_1 = Estudiante(nombre="Nicolás", legajo="LEG-001")
        
        inscripcion_python = Inscripcion(
            estudiante=estudiante_1, 
            curso=curso_python, 
            calificacion_final=9.5
        )
        
        inscripcion_bd = Inscripcion(
            estudiante=estudiante_1, 
            curso=curso_bd
        )
        
        session.add_all([inscripcion_python, inscripcion_bd])
        session.commit()
        print("-> Inscripciones guardadas exitosamente.\n")
    
    with Session(engine) as session:
        stmt = select(Estudiante).where(Estudiante.nombre == "Nicolás")
        nico = session.scalars(stmt).first()
        
        if nico:
            print(f"Historial académico de {nico.nombre}:")
            for insc in nico.inscripciones:
                nota = insc.calificacion_final if insc.calificacion_final is not None else "Sin calificar"
                fecha = insc.fecha_inscripcion.strftime('%Y-%m-%d')
                print(f" - Curso: {insc.curso.titulo} | Fecha: {fecha} | Nota: {nota}")
                
if __name__ == "__main__":
    main()