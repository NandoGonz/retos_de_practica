class Producto:
    def __init__(self, nombre: str, stock: int, precio: float):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio
        self.estado = True

    def __str__(self):
        estado = "Disponible" if self.estado else "Agotado"
        return f"Producto: {self.nombre} | Cantidad: {self.stock} | Valor: {self.precio} | Estado: {estado}"


class Inventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self, nombre, stock, precio):
        for p in self.productos:
            if p.nombre == nombre:
                p.stock += stock
                return False
        producto = Producto(nombre=nombre, stock=stock, precio=precio)
        self.productos.append(producto)
        return True

    def listar_productos(self):
        return self.productos

    def listar_por_nombre(self, nombre):
        for producto in self.productos:
            if nombre == producto.nombre:
                return producto
        return None

    def actualizar_prodcuto(self, nombre, stock):
        producto = self.listar_por_nombre(nombre)
        if producto not in self.productos:
            return None
        for p in self.productos:
            if p.nombre == nombre:
                p.stock += stock
        return True

    def cambiar_estado(self, nombre):
        producto = self.listar_por_nombre(nombre)
        if producto is None:
            return None
        if producto.estado is False:
            producto.estado = True
        elif producto.estado is True:
            producto.estado = False
        return True

    def vender_producto(self, nombre: str, cantidad: int):
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
