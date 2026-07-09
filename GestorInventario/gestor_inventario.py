class Producto:
    """Representa un producto dentro del inventario.

    Args:
        nombre (str): Nombre descriptivo del producto.
        stock (int): Cantidad disponible en inventario.
        precio (float): Precio unitario del producto.
    """

    def __init__(self, nombre: str, stock: int, precio: float):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio
        self.estado = True

    def __str__(self) -> str:
        estado = "Disponible" if self.estado else "Agotado"
        return f"""Producto: {self.nombre}|
        Cantidad: {self.stock}|
        Valor: {self.precio}|
        Estado: {estado}"""


class Inventario:
    """Gestiona una colección de productos y operaciones de inventario."""

    def __init__(self):
        self.productos = []

    def registrar_producto(self, nombre, stock, precio):
        """Agrega un nuevo producto al inventario o actualiza el stock si ya existe.

        Args:
            nombre: Nombre del producto.
            stock: Cantidad a agregar.
            precio: Precio unitario del producto.

        Returns:
            bool: True si el producto fue agregado, False si solo se actualizó el stock.
        """
        for p in self.productos:
            if p.nombre == nombre:
                p.stock += stock
                return False
        producto = Producto(nombre=nombre, stock=stock, precio=precio)
        self.productos.append(producto)
        return True

    def listar_productos(self):
        """Devuelve la lista completa de productos en el inventario."""
        return self.productos

    def listar_por_nombre(self, nombre):
        """Busca un producto en el inventario por su nombre.

        Args:
            nombre: Nombre del producto a buscar.

        Returns:
            Producto | None: Instancia del producto si se encuentra, de lo contrario None.
        """
        for producto in self.productos:
            if nombre == producto.nombre:
                return producto
        return None

    def actualizar_prodcuto(self, nombre, stock):
        """Actualiza el stock de un producto existente.

        Args:
            nombre: Nombre del producto a actualizar.
            stock: Cantidad a sumar al stock actual.

        Returns:
            bool | None: True si se actualiza correctamente, None si no se encuentra el producto.
        """
        producto = self.listar_por_nombre(nombre)
        if producto not in self.productos:
            return None
        for p in self.productos:
            if p.nombre == nombre:
                p.stock += stock
        return True

    def cambiar_estado(self, nombre):
        """Cambia el estado de disponibilidad de un producto.

        Args:
            nombre: Nombre del producto cuyo estado se desea alternar.

        Returns:
            bool | None: True si se cambió el estado, None si el producto no existe.
        """
        producto = self.listar_por_nombre(nombre)
        if producto is None:
            return None
        if producto.estado is False:
            producto.estado = True
        elif producto.estado is True:
            producto.estado = False
        return True

    def vender_producto(self, nombre: str, cantidad: int):
        """Registra la venta de una cantidad de un producto si está disponible.

        Args:
            nombre: Nombre del producto a vender.
            cantidad: Cantidad solicitada para la venta.

        Returns:
            bool | None: True si la venta fue exitosa, False si no hay suficiente stock o
            el producto está agotado,
            None si el producto no existe.
        """
        producto = self.listar_por_nombre(nombre=nombre)
        if producto is None:
            return None
        if producto.estado is False:
            return False
        if producto.stock == 0:
            return False
        if cantidad > producto.stock:
            return False
        producto.stock -= cantidad
        return True
