from datetime import timedelta


class Pedido:
contador_pedido = 0
     def __init__(self, materia=None, solicitante=None, pedido=None)
         pedido.contador_pedido += 1
         self.materia = materia
         self._id = pedido.contador_pedido
         self._solicitante = solicitante
         self._lista_material = None
         self._materia = materia
         td = timedelta(days=5)
         self._fecha_devolucion = self._fecha_prestamo + td

        @property
        def id(self):
            return self._id

        @property
        def materia(self):
            return self.materia

