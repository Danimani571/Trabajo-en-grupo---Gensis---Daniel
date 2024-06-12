from material import Material
class Libro(Material):
    contador_libro = 0

    def __init__(self, codigo=None, autor=None, titulo=None, anio=2000, editorial=None, disponible=True, cantidad_disponible=0, tipo_pasta=None):
        Material.__int__(self, codigo=codigo, autor=autor, titulo=titulo, anio=anio, editorial=editorial, disponible=disponible, cantidad_disponible=cantidad_disponible,tipo_pasta=tipo_pasta)
        self._tipo_pasta = tipo_pasta
        Libro.contador_libro += 1
        self._id = Libro.contador_libro

    @property
    def id(self):
     return self._id
    @property
    def tipo_pasta(self):
        return self._tipo_pasta
    @tipo_pasta.setter
    def tipo_pasta (self,valor):
        self._tipo_pasta= valor

    def _str_(self):
        return f'Libro{self._dict.str_()}'
    def actualizar_disponibilidad(self,disponible):
        self.disponible=disponible
if __name__ == "_main_":
    l = Libro(codigo='03, autor='Pablo ', titulo='La_luciernaga', editorial='edit_papel', anio=2005,
                 disponible=True, cantidad_disponible=5, tipo_pasta='MUY DURA')
print(l)