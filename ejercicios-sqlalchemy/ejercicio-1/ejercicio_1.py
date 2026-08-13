from datetime import datetime
from sqlalchemy import String, DateTime, select
from sqlalchemy.orm import Mapped, mapped_column, Session

from database import Base, engine

class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)


def main():
    # Crear las tablas en la base de datos
    Base.metadata.create_all(engine)

    # Crear una sesión para interactuar con la base de datos
    with Session(engine) as session:
        profesor1 = Profesor(nombre="Carlos Ruiz", email="carlos@universidad.edu", fecha_ingreso=datetime(2015, 4, 20))
        profesor2 = Profesor(nombre="Lucía Gómez", email="lucia@universidad.edu")
        
        # Agregar los profesores a la sesión
        session.add_all([profesor1, profesor2])
        session.commit()
        print("Profesores agregados a la base de datos.")
        
    with Session(engine) as session:
        # Consultar todos los profesores
        stmt = select(Profesor)
        profesores = session.scalars(stmt).all()
        
        print("Profesores en la base de datos:")
        for profesor in profesores:
            print(f"ID: {profesor.id} | Nombre: {profesor.nombre} | Email: {profesor.email} | Fecha de Ingreso: {profesor.fecha_ingreso}")

if __name__ == "__main__":
    main()

