# Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número
# perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
# (excluyendo el propio número).

print("Números perfectos menores que 1000:")

for num in range(2, 1000):
    suma_divisores = 0
    
    for i in range(1, num):
        if num % i == 0:   # si i es divisor
            suma_divisores += i
    
    if suma_divisores == num:
        print(num)
