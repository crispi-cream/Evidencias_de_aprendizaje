# Solicitar nombres de las materias y calificaciones
materia1 = input("Introduce el nombre de la primera materia: ")
calificacion1 = float(input(f"Introduce la calificación de {materia1}: "))

materia2 = input("Introduce el nombre de la segunda materia: ")
calificacion2 = float(input(f"Introduce la calificación de {materia2}: "))

materia3 = input("Introduce el nombre de la tercera materia: ")
calificacion3 = float(input(f"Introduce la calificación de {materia3}: "))

materia4 = input("Introduce el nombre de la cuarta materia: ")
calificacion4 = float(input(f"Introduce la calificación de {materia4}: "))

# Calcular el promedio
promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4) / 4

# Mostrar el promedio
print("\nResultados:")
print(f"{materia1}: {calificacion1}")
print(f"{materia2}: {calificacion2}")
print(f"{materia3}: {calificacion3}")
print(f"{materia4}: {calificacion4}")
print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")