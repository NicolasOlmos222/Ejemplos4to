
class Alumno:
    def __init__(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def getNombre(self):
        return self.nombre
    
    def getInfo(self):
        return self.nombre, self.nota1, self.nota2, self.nota3
    
    def promediar(self):
        promedio = (self.nota1 + self.nota2 + self.nota3) / 3
        return promedio
    
    def condicion(self):
        if self.promediar() >= 7:
            return True
        else:
            return False