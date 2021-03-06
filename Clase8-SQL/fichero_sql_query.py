from sqlalchemy.orm import sessionmaker
from fichero_sql_tablas import Estudiante, create_engine

engine = create_engine('sqlite:///estudiantes.db', echo=True)

#Crea session
Session = sessionmaker(bind=engine)
session =  Session()

#Query
#for Estudiante in session.query(Estudiante).order_by(Estudiante.id):
    #print(Estudiante.nombre, Estudiante.apellido1, Estudiante.apellido2)

# Ejemplo seleccionar objeto
for Estudiante in session.query(Estudiante).filter(Estudiante.universidad == 'UPC'):
    print(Estudiante.nombre, Estudiante.apellido1, Estudiante.apellido2)