class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # True = disponible, False = prestado

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f" Titulo: {self.titulo} - Autor: {self.autor} | ISBN: {self.isbn} | Estado: {estado}"


class GestorPrestamos:
    def __init__(self):
        self.libros = []

    def registrar_libro(self, isbn: str, titulo: str, autor: str):
        # 1️⃣ Verificar duplicado
        # 2️⃣ Crear libro
        # 3️⃣ Agregar a la lista
        # 4️⃣ Retornar Libro o None
        for libro in self.libros:
            if libro.isbn == isbn:
                return None
        libro = Libro(isbn=isbn, titulo=titulo, autor=autor)
        self.libros.append(libro)
        return libro

    def buscar_por_isbn(self, isbn: str):
        # 1️⃣ Recorrer libros
        # 2️⃣ Retornar Libro o None
        for libro in self.libros:
            if isbn == libro.isbn:
                return libro
        return None

    def listar_libros(self):
        # Retornar lista completa
        return self.libros

    def prestar_libro(self, isbn: str):
        # 1️⃣ Buscar libro
        # 2️⃣ Verificar si está disponible
        # 3️⃣ Cambiar estado
        # 4️⃣ Retornar True o False
        libro = self.buscar_por_isbn(isbn)
        if libro is None:
            return None
        if libro.disponible is True:
            libro.disponible = False
            return True
        return False

    def devolver_libro(self, isbn: str):
        # 1️⃣ Buscar libro
        # 2️⃣ Verificar si está prestado
        # 3️⃣ Cambiar estado
        # 4️⃣ Retornar True o False
        libro = self.buscar_por_isbn(isbn)
        if libro is None:
            return None
        if libro.disponible is False:
            libro.disponible = True
            return True
        return False
