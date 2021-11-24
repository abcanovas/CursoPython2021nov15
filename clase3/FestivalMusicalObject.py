import datetime
from FestivalMusical import FestivalMusical

festival1 = FestivalMusical('Creamfields', 'UK', 'Dance')
festival2 = FestivalMusical('Download', 'UK', 'Metal')


print(festival1.nombre)
festival2.festival_metodo()


print(festival1.nombre.upper())
#print(festival1)


festival1.nombre = ('Benicassim')
print(festival1.nombre)
#del festival1


FestivalMusical.valor_ticket(50)
print(FestivalMusical.valor_ticket)    #Accede a la clase
print(festival2.valor_ticket)    #Accede a la instancia


dia1 = datetime.date(2021,11,18)
FestivalMusical.dia_evento(dia1)