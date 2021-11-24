import re

#Encontrar coincidencias
texto = "Hoy es un día magnifico y maravilloso"
exp_reg= re.search("^Hoy.*oso$", texto)
print(exp_reg)

exp_reg2 = re.findall('ma', texto)
print(exp_reg2)

exp_reg3 = re.sub("\s", "    ", texto)