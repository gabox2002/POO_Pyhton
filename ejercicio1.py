def accion_a(num1, num2):
    # Sumar dos números
    resultado = num1 + num2
    return resultado

def accion_b(num1, num2):
    # Multiplicar dos números
    resultado = num1 * num2
    return resultado

def main():
    while True:
        # Muestra opciones al usuario
        print("1. Realizar Acción A (Suma)")
        print("2. Realizar Acción B (Multiplicación)")
        print("0. Salir")

        # Solicita la opción al usuario
        opcion = input("Ingrese el número de la opción deseada: ")

        # Verifica la opción ingresada
        if opcion == "0":
            print("Saliendo del programa.")
            break
        elif opcion == "1" or opcion == "2":
            # Solicita números al usuario
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            # Realiza la acción según la opción ingresada
            if opcion == "1":
                resultado = accion_a(num1, num2)
                print(f"El resultado de la Acción A (suma)es: {resultado}")
            elif opcion == "2":
                resultado = accion_b(num1, num2)
                print(f"El resultado de la Acción B (multiplicación) es: {resultado}")
        else:
            print("Opción no válida. Por favor, ingrese 0, 1 o 2.")

if __name__ == "__main__":
    main()