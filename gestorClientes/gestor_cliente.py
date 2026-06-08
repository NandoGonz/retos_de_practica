"""Gestor de clientes

permitira crearlo, actualizarlo,
filtrar una busqueda por documento, actaulización de algunos datos
y listar todos los clientes
"""

from pydantic import BaseModel


class Cliente(BaseModel):
    """Representa un cliente con información personal y financiera.

    Attributes:
        nombre (str): Nombre del cliente.
        apellido (str): Apellido del cliente.
        documento (int): Número de documento identificador.
        email (str): Correo electrónico del cliente.
        direccion (str): Dirección postal del cliente.
        saldo (float): Saldo disponible del cliente.
        activo (bool): Estado del cliente (True si está activo).
    """

    nombre: str
    apellido: str
    documento: int
    email: str
    direccion: str
    saldo: float
    activo: bool = True

    def __str__(self) -> str:
        """Devuelve una representación legible del cliente.

        Returns:
            str: Cadena formateada con los datos principales del cliente.
        """
        estado = "Activo" if self.activo else "Inactivo"
        return f"""
        Cliente: {self.nombre} {self.apellido}
        Documento: {self.documento}
        Email: {self.email}
        Dirección: {self.direccion}
        Saldo $: {self.saldo:,.2f}
        Estado: {estado}
        """


class GestorCliente:
    """Gestor para operaciones básicas sobre clientes en memoria.

    Mantiene una lista de instancias `Cliente` y proporciona métodos para
    buscar, registrar, listar y actualizar clientes.
    """

    def __init__(self) -> None:
        """Inicializa el gestor con una lista vacía de clientes."""
        self.clientes = []

    def buscar_cliente_docu(self, n_documento: int):
        """Busca un cliente por su número de documento.

        Args:
            n_documento (int): Número de documento a buscar.

        Returns:
            Cliente | None: Instancia de `Cliente` si se encuentra, sino `None`.
        """
        for c in self.clientes:
            if n_documento == c.documento:
                return c
        return None

    def registrar_cliente(
        self,
        nombre: str,
        apellido: str,
        documento: int,
        email: str,
        direccion: str,
        saldo: float,
    ):
        """Registra un nuevo cliente si no existe otro con el mismo documento.

        Args:
            nombre (str): Nombre del cliente.
            apellido (str): Apellido del cliente.
            documento (int): Documento identificador.
            email (str): Correo electrónico.
            direccion (str): Dirección postal.
            saldo (float): Saldo inicial.

        Returns:
            bool: True si el registro fue exitoso, False si ya existe el documento.
        """
        verificar = self.buscar_cliente_docu(n_documento=documento)
        if verificar:
            return False

        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            documento=documento,
            email=email,
            direccion=direccion,
            saldo=saldo,
        )
        self.clientes.append(cliente)
        return True

    def listar_clientes(self):
        """Devuelve la lista de clientes registrados.

        Returns:
            list[Cliente]: Lista de instancias de `Cliente` almacenadas.
        """
        return self.clientes

    def actualizar_estado(self, documento: int):
        """Alterna el estado `activo` de un cliente y devuelve el nuevo valor.

        Args:
            documento (int): Documento del cliente a actualizar.

        Returns:
            bool | None: True si el cliente quedó activo, False si quedó inactivo,
            None si no se encontró el cliente.
        """
        cliente = self.buscar_cliente_docu(n_documento=documento)
        if cliente is None:
            return None
        if cliente.activo is False:
            cliente.activo = True
            return True
        if cliente.activo is True:
            cliente.activo = False
            return False

    def actualizar_cliente(
        self, nombre: str, apellido: str, direccion: str, email: str, documento: int
    ):
        """Actualiza los datos personales de un cliente existente.

        Args:
            nombre (str): Nuevo nombre del cliente.
            apellido (str): Nuevo apellido del cliente.
            direccion (str): Nueva dirección.
            email (str): Nuevo correo electrónico.
            documento (int): Documento del cliente a actualizar.

        Returns:
            bool | None: True si la actualización fue exitosa, None si no se encontró el cliente.
        """
        cliente = self.buscar_cliente_docu(n_documento=documento)
        if cliente is None:
            return None
        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.direccion = direccion
        cliente.email = email
        return True
