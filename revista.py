from MATERIAL import Material
class Revista(Material):
    contador_revista = 0

    def __init__(self, codigo=None, autor=None, titulo=None, anio=2000, editorial=None, disponible=True,
                 cantidad_disponible=0, tipo=None):
        Material._init_(self, codigo=codigo, autor=autor, titulo=titulo, anio=anio, editorial=editorial,
                          disponible=disponible, cantidad_disponible=cantidad_disponible)
        self._tipo = tipo
        Revista.contador_revista += 1
        self._id = Revista.contador_revista

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    def _str_(self):
        return f'Revista:{self._dict.str_()}'

if _name_ == "_main_":
    r = Revista(codigo=45, autor='Amalia Andrade', titulo='Un titulo', editorial='s.a edicion', anio=2024,
                disponible=True, cantidad_disponible=2, tipo='Drama')
print(r)