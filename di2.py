palabras = ["hola", "hola", "adios", "python", "programacion", "computadora"]
frecuencia = {}

for palabra in palabras:
  if palabra in frecuencia:
    frecuencia[palabra] += 1
  else:
    frecuencia[palabra] = 1

print(frecuencia)
