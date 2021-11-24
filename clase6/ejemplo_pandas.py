import pandas as pd

fichero_csv = "catalogo_cf.csv"
fichero_tsv = "catalogo_cf.tsv"

escribir_csv = "catalogo_csv_ext.csv"
escribir_tsv = "catalogo_tsv_ext.tsv"

leer_csv = pd.read_csv(fichero_csv, encoding="ISO-8859-1")
leer_tsv = pd.read_csv(fichero_tsv, sep = "\t", encoding="ISO-8859-1")

print(leer_csv.head(10))
print(leer_tsv.head(10))

with open(escribir_csv, 'w') as write_csv:
	write_csv.write(leer_csv.head(10).to_csv(sep=',', index=False))


with open(escribir_tsv, 'w') as write_tsv:
	write_tsv.write(leer_tsv.head(10).to_csv(sep='\t', index=False))