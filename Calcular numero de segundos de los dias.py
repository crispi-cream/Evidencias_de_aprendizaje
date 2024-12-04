# Programa para calcular el número de segundos en un número de días

def calcular_segundos_en_dias(dias):
    segundos_por_dia = 24 * 60 * 60  # Horas, minutos y segundos en un día
    return dias * segundos_por_dia

def solicitar_dias():
    while True:
        try:
            dias = int(input("Ingrese el número de días: "))
            if dias < 0:
                print("Por favor, ingrese un número positivo.")
            else:
                return dias
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    dias = solicitar_dias()
    segundos = calcular_segundos_en_dias(dias)
    print(f"El número de segundos en {dias} día(s) es: {segundos}")

if __name__ == "__main__":
    main()
