# En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
# fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
# lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
# en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
# ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de 1636!


meses = [
    "Enero","Febrero","Marzo","Abril","Mayo","Junio",
    "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"
]

fecha = input("Ingrese la fecha: ").strip()

if "/" in fecha: 
    m, d, a = fecha.split("/")
    print(f"{int(a):04}-{int(m):02}-{int(d):02}")
else: 
    mes_texto, resto = fecha.split(" ", 1)
    d, a = resto.replace(",", "").split()
    m = meses.index(mes_texto) + 1
    print(f"{int(a):04}-{m:02}-{int(d):02}")

