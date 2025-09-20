# Escribe un programa que encuentre la suma de todos los números primos menores que 100.

suma = 0

for num in range(2, 100): 
    es_primo = True        

    for i in range(2, num): 
        if num % i == 0:
            es_primo = False
            break
    
    if es_primo:
        suma += num

print("La suma de los números primos menores que 100 es:", suma)
