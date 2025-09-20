# Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
# ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos números.
# Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
# números pares e impares.


numeros = []

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    
    if respuesta == "NO":
        break
    elif respuesta == "SI":
        num = int(input("Ingrese un número: "))
        numeros.append(num)
    else:
        print("Por favor, responda solo con SI o NO.")

pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Números ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)


