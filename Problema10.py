# Escribe una función de Python para calcular el factorial de un número (un entero no negativo). Lafunción acepta el número como argumento.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Ingrese un número: "))
print("El factorial de", num, "es:", format(factorial(num), ","))


