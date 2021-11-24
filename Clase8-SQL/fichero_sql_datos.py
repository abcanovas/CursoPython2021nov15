from sqlalchemy.orm import sessionmaker

from fichero_sql_tablas import Estudiante, create_engine

engine = create_engine('sqlite:///estudiantes.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Crea las instancias
usuario = Estudiante("juan", "Juan","Perez","Lopez","Complutense")
session.add(usuario)
usuario = Estudiante("Maria", "María","García","Gomez","UPC")
session.add(usuario)
usuario = Estudiante("Beatriz", "Beatriz","Suarez","Gonzalez","Carlos III")
session.add(usuario)
# commit the record the database
session.commit()
# Fichero para consultar