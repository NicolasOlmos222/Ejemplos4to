#TESTING
from config import *

#Inicializar bd
curso = Curso()

def menu():
    print("1. Agregar alumno")
    print("2. Ver todos los laumnos")
    print("3. Buscar alumno")
    print("4. Salir")
    op = int(input("Ingrese la opcion: "))
    return op

while True:
    op = menu()
    if op == 1:
        alumno = Alumno(input("Ingrese su nombre: "),
                        int(input("Ingrese una nota 1: ")),
                        int(input("Ingrese una nota 2: ")),
                        int(input("Ingrese una nota 3: ")),)
        curso.agregarAlumno(alumno)
    elif op == 2:
        lista = curso.listarAlumnos()
        for elemento in lista:
            print(elemento.getNombre())
    elif op == 3:
        nombre = input("Ingrese el nombre: ")
        alumno = curso.buscarAlumno(nombre)
        if alumno:
            print(alumno.getInfo())
        else:
            print("No se encontro alumno")