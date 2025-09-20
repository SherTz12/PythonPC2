# Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
# pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
# materias.

alumnos = []

n = int(input("¿Cuántos alumnos desea ingresar?: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    
    notas = []
    for j in range(3):
        nota = int(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    
    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }
    
    alumnos.append(alumno)

print("\nListado completo de alumnos:")
for alumno in alumnos:
    print(alumno)
