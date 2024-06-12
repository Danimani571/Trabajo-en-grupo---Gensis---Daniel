from clases import Libro, Revista, Estudiante, Docente, Pedido

if _name_ == "_main_":
    main()
estudiante1 = Estudiante(cedula='0942456674', nombre='Daniel'
                        , apellido='Pluas', nivel=1)
estudiante2 = Estudiante(cedula= '094946516',nombre='Genesis'
                        , apellido='Mite', nivel=2)

def main():
    # Creating instances of Libro and Revista
    libro1 = Libro("001", "Autor1", "Titulo1", 2020, "Editorial1", True, 10, 1, "Dura")
    revista1 = Revista("002", "Autor2", "Titulo2", 2021, "Editorial2", True, 5, 1, "Ciencia")


    estudiante1 = Estudiante("1234567890", "Juan", "Perez", "juan@example.com", "0999999999", "Direccion1", 0, True, "Ingenieria", 1, 3)
    docente1 = Docente("0987654321", "Ana", "Gomez", "ana@example.com", "0888888888", "Direccion2", 0, True, "Matematicas", 1, "Licenciatura", "Maestria")


    pedido1 = Pedido(1, estudiante1, [libro1], "Matematicas", "2023-06-01", "2023-06-15")

    print(libro1.titulo)
    print(revista1.titulo)
    print(estudiante1)
    print(docente1)

