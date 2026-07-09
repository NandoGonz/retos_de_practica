from venta import Venta


class GestorVentas:
    """Clase encargada de la lógica del proyecto"""

    def __init__(self) -> None:
        self.ventas = []

    def generar_venta(self, venta: Venta):
        """Método encargado de crear las ventas"""

        self.ventas.append(venta)
        return True

    def listar_ventas(self):
        """Método encargado de listar y mostrar las ventas generadas"""
        return self.ventas
