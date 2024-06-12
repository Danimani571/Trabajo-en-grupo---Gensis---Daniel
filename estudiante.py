from persona import Persona

class Estudiante(Persona):
    contador_estudiantes = 0
    def __init__(self, cedula = None, nombre = None, apellido = None, nivel = None, id=1 ):
        Persona.__init__(self, cedula = cedula, nombre = nombre, apellido = apellido, nivel = nivel)
        Estudiante.contador_estudiantes += 1
        self.estudiante = Estudiante.contador_estudiantes
        self._nivel = nivel

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def cedula(self):
        return self.cedula

    @property
    def nombre(self):
        return self.nombre

    @property
    def apellido(self):
        return self.apellido

    @property
    def nivel(self):
        return self._nivel

    def _str_(self):
        return f'Estudiante: {self._dict.str_()}'

    def pedir_libro(self):
        print(f'Estudiante{self.nombre} ha pedido un libro.')
        pass

    def devolver_libro(self):
        print(f'Estudiante{self.nombre} ha devuelto un libro.')
        pass

if __name__ == '__main__':
    d = Estudiante("099849261561", "Paola", "Anzules", "Paola@gmail.com", "091519848748", "vía Daule",  14, 3, "matematica")
    print(d)
    print(Estudiante.mro())