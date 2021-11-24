def funcion_excepciones():
    try:
        print(10/0)
    except ZeroDivisionError:
        print("Error. No se puedo dividir entre cero")
    else:
        # pass
        print("La excepción no ha ocurrido")
    finally:
        print("Finalizadas las excepciones")

funcion_excepciones()