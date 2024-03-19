def encontrar_palabra(texto):
  palabras = texto.split()
  frecuenciapalabras = {}

  for palabra in palabras:
    palabra = palabra.lower()  # Convertir la palabra a minúsculas
    if palabra in frecuenciapalabras:
      frecuenciapalabras[palabra] += 1
    else:
      frecuenciapalabras[palabra] = 1

  # Encontrar la palabra con la frecuencia más alta
  palabramascomun = max(frecuenciapalabras, key=frecuenciapalabras.get)
  frecuenciamasalta = frecuenciapalabras[palabramascomun]

  return palabramascomun, frecuenciamasalta


# Texto del manuscrito antiguo
texto_manuscrito = "Los exploradores descubren un manuscrito antiguo y desean encontrar la palabra más común en él. Implementa un programa que utilice un diccionario para encontrar la palabra con la frecuencia más alta en el texto."

# Encontrar la palabra más común en el texto del manuscrito
palabra_mas_comun, frecuencia_mas_alta = encontrar_palabra(texto_manuscrito)
print("La palabra más común es:", palabra_mas_comun)
print("Frecuencia más alta:", frecuencia_mas_alta)
