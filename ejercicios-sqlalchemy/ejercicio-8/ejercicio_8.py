from database import Base, engine
from typing import List, Optional
from datetime import datetime
from sqlalchemy import ForeignKey, String, DateTime, select, func
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
        depto_sistemas = Departamento(nombre="Sistemas")
        profe_carlos = Profesor(nombre="Carlos Ruiz", email="carlos@u.edu", departamento=depto_sistemas)
        
        curso_py = Curso(titulo="Introducción a Python", creditos=3, profesor=profe_carlos)
        curso_bd = Curso(titulo="Bases de Datos", creditos=4, profesor=profe_carlos)
        
        nico = Estudiante(nombre="Nicolás", legajo="LEG-001")
        marti = Estudiante(nombre="Martina", legajo="LEG-002")
        
        session.add_all([
            Inscripcion(estudiante=nico, curso=curso_py, calificacion_final=9.5),
            Inscripcion(estudiante=nico, curso=curso_bd, calificacion_final=8.0),
            Inscripcion(estudiante=marti, curso=curso_bd, calificacion_final=10.0)
        ])
        session.commit()
    
    with Session(engine) as session:
        
        print("Cursos dictados por profesor especifico:")
        stmt = (
            select(Curso)
            .join(Curso.profesor)
            .where(Profesor.nombre == "Carlos Ruiz")
        )
        
        cursos_profe = session.scalars(stmt).all()
        
        if cursos_profe:
            for c in cursos_profe:
                print(f" - {c.titulo}")
        else:
            print("No se encontraron cursos para ese profesor.")
            
        print("\nPromedio de calificaciones de un estiudiante específico:")
        
        stmt = (
            select(func.avg(Inscripcion.calificacion_final))
            .join(Inscripcion.estudiante)
            .where(Estudiante.nombre == "Nicolás")
        )
            
        promedio = session.scalars(stmt).first()
        print(f" - Promedio: {promedio}")

        print("\nCantidad de estudiantes inscriptos en cada curso:")
        stmt = (
            select(Curso, func.count(Inscripcion.estudiante_id).label("cantidad_estudiantes"))
            .join(Curso.inscripciones)
            .group_by(Curso.id)
        )
        
        resultados = session.execute(stmt).all()
        for curso, cantidad in resultados:
            print(f" - {curso.titulo}: {cantidad} estudiantes")
            
if __name__ == "__main__":
    main()