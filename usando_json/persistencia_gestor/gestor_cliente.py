"""Gestor de clientes

permitira crearlo, actualizarlo,
filtrar una busqueda por documento, actaulización de algunos datos
y listar todos los clientes
"""

import json
from usando_json.persistencia_gestor.models import Cliente


class GestorCliente:
    """Gestor para operaciones básicas sobre clientes en memoria.

    Mantiene una lista de instancias `Cliente` y proporciona métodos para
    buscar, registrar, listar y actualizar clientes.
    """

    PERSISTENCIA_JSON = "datos.json"

    def __init__(self) -> None:
        """Inicializa el gestor con una lista vacía de clientes."""
        self.clientes = []

    def registrar(self, cliente: Cliente):
        if cliente.documento in self.clientes:
            return False
        self.clientes.append(cliente)
        return True

    def guardar_json(self):
        datos = []
        for cliente in self.clientes:
            datos.append(cliente.model_dump())

        with open(self.PERSISTENCIA_JSON, "w", encoding="UTF-8") as archivo:
            json.dump(datos, archivo, indent=4)

    def cargar_json(self):
        with open(self.PERSISTENCIA_JSON, "r", encoding="UTF-8") as archivo:
            datos = json.load(archivo)

        self.clientes = []

        for dato in datos:
            cliente = Cliente(**dato)
            self.clientes.append(cliente)

    def listar(self):
        return self.clientes

    def actualizar_cliente(self, identificacion: int, cliente_act: Cliente):
        for cliente in self.clientes:
            if cliente.documento == identificacion:
                cliente.nombre = cliente_act.nombre
                cliente.apellido = cliente_act.apellido
                cliente.email = cliente_act.email
                cliente.direccion = cliente_act.direccion
                self.guardar_json()
                return True
        return False
