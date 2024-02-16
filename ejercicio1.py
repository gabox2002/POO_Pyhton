def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

def main():
    while True:
        print("1. Realizar suma")
        print("2. Realizar multiplicación")

        # Solicita la opción al usuario
        opcion = input("Ingrese el número de la opción deseada: ")

        # Verifica la opción ingresada
        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = sumar(num1, num2)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == "2":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = multiplicar(num1, num2)
            print(f"El resultado de la multiplicación es: {resultado}")
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")

if __name__ == "__main__":
    main()
