import cchardet as chardet

with open(r'ejemplo_fnmatch.py', 'rb') as f:
	msg = f.read()
	result = chardet.detect(msg)
	print(result)