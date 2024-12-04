import math

# Solicitar al usuario que ingrese un número
numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))

# Verificar que el número sea mayor o igual a cero
if numero >= 0:
    raiz = math.sqrt(numero)  # Calcular la raíz cuadrada usando math.sqrt
    print(f"La raíz cuadrada de {numero} es: {raiz}")
else:
    print("El número ingresado es negativo, no se puede calcular la raíz cuadrada real.")