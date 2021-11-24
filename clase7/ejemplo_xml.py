import xml.etree.ElementTree as ET
# Importar XML desde un fichero
arbol = ET.parse('ejemplo_country_data.xml')
raiz = arbol.getroot()

# Acceder a elementos determinados
#for child in raiz:
#    print(child.tag, child.attrib)

# Acceder al child utilizando índices
#print(raiz[0][1].text)


#Acceder a subelemento utilizando el metodo element
for neighbor in raiz.findall('neighbor'):
    rank = country.find('rank').text
    name  = country.get('name')
    print(name, rank)


#Modificar un fichero XML y escribirlo a un nuevo fichero
for rank in raiz.inter('rank'):
    new_rank= int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('Actualizado','si')
arbol.write('ejemplo_country_data_modificado.xml')