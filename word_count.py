import os

CUR_DIR = os.path.dirname(__file__)

with open(os.path.join(CUR_DIR, "lorem_ipsum.txt"), "r") as file:
	contenido = file.read()
	palabras_separadas = contenido.split(" ")
      
palabras_unicas = set(palabras_separadas)
caracteres_unicos = set(" ".join(palabras_separadas))

print("El número de caracteres distintos es:", len(caracteres_unicos))
print("El número de palabras distintas es:", len(palabras_unicas))