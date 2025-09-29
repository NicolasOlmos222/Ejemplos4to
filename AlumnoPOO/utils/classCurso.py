
class Curso:
    def __init__(self):
        self.lista = []

    def agregarAlumno(self, alumno):
        self.lista.append(alumno)

    def listarAlumnos(self):
        return self.lista
    
    def buscarAlumno(self, nombre):
        for elemento in self.lista:
            if elemento.getNombre() == nombre:
                return elemento
        return False