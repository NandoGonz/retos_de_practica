from logica_prestamos import GestorPrestamos

gestor = GestorPrestamos()


def menu():
    print("Biblioteca AGC")
    while True:
        print("1. Registrar un libro.")
        print("2. Prestar un libro.")
        print("3. Devolver un libro.")
        print("4. Buscar por ISBN.")
        print("5. Mostar todos los libros.")
        print("0. Salir.")
        try:
            opcion = int(
                input("Ingrese una opcion del (0 al 5) para continuar o 0 para salir: ")
            )
            match opcion:
                case 1:
                    try:
                        isbn = input("Ingresar el ISBN del libro: ")
                        titulo = input("ingresar el titulo del libro: ")
                        autor = input("Ingresar el autor del libro: ")
                        if isbn == "" or titulo == "" or autor == "":
                            raise ValueError("Todos los campos son obligatorios.")
                        resultado = gestor.registrar_libro(isbn, titulo, autor)
                        if resultado is None:
                            print("El ISBN esta asignado a otro libro")
                        else:
                            print("Libro registrado de manera exitosa")
                    except ValueError as e:
                        print(e)
                case 2:
                    isbn = input("Ingresar el ISBN del libro que desea buscar: ")
                    libro = gestor.prestar_libro(isbn)
                    if libro is True:
                        print("Libro prestado de forma exitosa")
                    elif libro is False:
                        print("el libro ya ha sido prestado")
                    elif libro is None:
                        print(
                            "El libro que busca no esta registrado en esta biblioteca"
                        )
                case 3:
                    isbn = input("Ingresar el ISBN del libro que desea devolver: ")
                    libro = gestor.devolver_libro(isbn)
                    if libro is True:
                        print("Libro devuelto de forma exitosa")
                    elif libro is False:
                        print("El libro ya esta disponible")
                    elif libro is None:
                        print(
                            "El libro que busca no esta registrado en esta biblioteca"
                        )

                case 4:
                    isbn = input("Ingresar el ISBN del libro que desea buscar: ")
                    libro = gestor.buscar_por_isbn(isbn)
                    if libro is None:
                        print("El libro no existe")
                    else:
                        print(libro)
                case 5:
                    libros = gestor.listar_libros()
                    for libro in libros:
                        print(libro)

                case 0:
                    print("Saliendo del menú de biblioteca AGC...")
                    break
        except ValueError:
            print("Ingrese un aopción valida dentro del menú")


if __name__ == "__main__":
    menu()
