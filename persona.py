class Persona:
    def __init__(self, cedula: object = None, nombre: object = None, apellido: object = None, email: object = None, telefono: object = None, direccion: object = None,
                 numero_libros: object = None, activo: object = True, carrera: object = 0):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera


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
def email(self):
    return self.email


@property
def telefono(self):
    return self.telefono


@property
def direccion(self):
    return self.direccion


@property
def numero_libros(self):
    return self.numero_libros


@property
def activo(self):
    return self.activo


@property
def carrera(self):
    return self.carrera


@activo.setter
def activos(self, activo):
    self._activo = activo


@property
def carrera(self):
    return self._carrera


@carrera.setter
def carrera(self, carrera):
    self._carrera = carrera


def _str_(self):
    return f'Persona {self._dict.str_()}'


if __name__ == '__main__':
    Persona = Persona(cedula='0942456674', nombre='Daniel', apellido='Pluas', email='danielpluas571@gmail.com',
                telefono='0962012501', direccion='Daule', carrera='Finanzas')
print(Persona)
