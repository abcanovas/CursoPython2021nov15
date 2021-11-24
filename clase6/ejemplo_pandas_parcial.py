import pandas as pd

# Se crea el dataframe con pandas de un excel
dataframe_excel = pd.read_excel("catalogo_cf.xlsx")
print(dataframe_excel)

# Selecciona la primera y la cuarta columna
print(dataframe_excel.iloc[:, [0,3]])

# Se exporta a excel
dataframe_excel.iloc[:, [0, 3]].to_excel('catalogo_cf_resumen.xlsx')