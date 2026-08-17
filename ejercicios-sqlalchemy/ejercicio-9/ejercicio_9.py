from database import Base, engine
from typing import List, Optional
from datetime import datetime
from sqlalchemy import ForeignKey, String, DateTime, select, func
from sqlalchemy.orm import Mapped, mapped_column, Session, relationship
from sqlalchemy.exc import IntegrityError

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

def matricular_alumno(session: Session, estudiante: Estudiante, curso: Curso, calificacion_final: Optional[float] = None):
    print(f"Intentando matricular a '{estudiante.nombre}' en el curso '{curso.titulo}'...")
    try:
        inscripcion = Inscripcion(estudiante=estudiante, curso=curso, calificacion_final=calificacion_final)
        session.add(inscripcion)
        session.commit()
        print("Alumno matriculado exitosamente.")
    except IntegrityError:
        session.rollback()
        print(f"Error al matricular al alumno. El estudiante '{estudiante.nombre}' ya está inscrito en el curso '{curso.titulo}'.")
    except Exception as e:
        session.rollback()
        print(f"Ocurrió un error inesperado: {e}")


def main():
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        depto = Departamento(nombre="Sistemas")
        profe = Profesor(nombre="Carlos Ruiz", email="carlos@u.edu", departamento=depto)
        curso_py = Curso(titulo="Introducción a Python", creditos=3, profesor=profe)
        nico = Estudiante(nombre="Nicolás", legajo="LEG-001")
        
        session.add_all([depto, profe, curso_py, nico])
        session.commit()
    
    with Session(engine) as session:
        
        nico = session.scalars(select(Estudiante).where(Estudiante.nombre == "Nicolás")).first()
        curso_py = session.scalars(select(Curso).where(Curso.titulo == "Introducción a Python")).first()
        
        if nico and curso_py:
            print("--- PRIMER INTENTO (Matriculación válida) ---")
            matricular_alumno(session, nico, curso_py)
            
            print("--- SEGUNDO INTENTO (Forzando la excepción) ---")
            matricular_alumno(session, nico, curso_py)
            
        print("--- VERIFICACIÓN FINAL ---")
        stmt = select(func.count(Inscripcion.estudiante_id)).where(Inscripcion.estudiante_id == nico.id)
        cantidad = session.scalar(stmt)
        print(f"Registros de inscripción para {nico.nombre} en la base de datos: {cantidad}")
        if cantidad == 1:
            print("Verificación exitosa: El rollback evitó que se guardaran datos corruptos/duplicados.")
            
if __name__ == "__main__":
    main()