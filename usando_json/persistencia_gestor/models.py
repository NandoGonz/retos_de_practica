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
