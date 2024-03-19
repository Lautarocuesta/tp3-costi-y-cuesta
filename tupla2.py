import math

cordlago = (2, 3)
radio = math.sqrt(cordlago[0] ** 2 + cordlago[1] ** 2)
angulo = math.atan2(cordlago[1], cordlago[0])  
angulo_grados = math.degrees(angulo)  
print("Radio:", radio)
print("Ángulo en radianes:", angulo)
print("Ángulo en grados:", angulo_grados)
