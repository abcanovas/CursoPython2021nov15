import hashlib

nombre = 'quijote-ext01.txt'
nombre_codificado = nombre.encode()

nombre_hash = hashlib.sha512( )

print('Objeto: ', nombre_hash)
print('Formato hexadecimal', nombre_hash.hexdigest())