registro = {
    "Juan": 25,
    "María": 30,
    "Pedro": 40,
    "Ana": 35
}


print("Diccionario de edades inicial:")
print(registro)

# Agregar una nueva persona 
registro["Luis"] = 28


print("\nDiccionario después de agregar una nueva persona:")
print(registro)

# Eliminar una persona 
del registro["Pedro"]


print("\nDiccionario después de eliminar una persona:")
print(registro)

# Buscar la edad de una persona
persona = "Luis"
if persona in registro:
    print(f"\nLa edad de {persona} es {registro[persona]}.")
else:
    print(f"\n{persona} no está en el registro.")
