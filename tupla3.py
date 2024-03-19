import math

x_objeto = 1
y_objeto = 2
def coordecartapol(x, y):
    radio = math.sqrt(x ** 2 + y ** 2)
    angulor= math.atan2(y, x)
    angulog = math.degrees(angulor)
    return radio, angulor, angulog


radioobjeto, anguloradobjeto, angulogradosobjeto = coordecartapol(x_objeto, y_objeto)


print("Coordenadas polares del objeto misterioso:")
print("Radio:", radioobjeto)
print("Ángulo en radianes:", anguloradobjeto)
print("Ángulo en grados:", angulogradosobjeto)
