import os
import shutil
import pandas as pd
from pathlib import Path

fich_path=Path(Path.home(),"Repositorio_tst")
print(fich_path)

if not fich_path.exists():
	os.makedirs(fich_path)
	print("directorio creado")

fitch_copia = fich_path.joinpath("copia_catalogo_cf.csv")

shutil.copy(src="catalogo_cf.csv", dst=fitch_copia)

leer_csv = pd.read_csv("copia_catalogo_cf_csv", nrows=100, encoding='ANSI')

fichero_tsv = fich_path.joinpath("copia_catalogo_cf.tsv")

with open (fichero_tsv, 'w') as write_tsv:
	write_tsv.write(leer_csv.to_csv(sep= '\t'))