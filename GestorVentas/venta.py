"""Se importan unicamente los módulos necesarios para crear el modelo"""

from pydantic import BaseModel, Field, model_validator


class Venta(BaseModel):
    """Modelo para crear una venta"""

    nombre: str = Field(
        ..., min_length=4, max_length=20, description="Nombre del producto"
    )
    cantidad: int = Field(..., gt=0, description="Cantidad en libras del producto")
    precio: float = Field(..., gt=0)
    # Protegido: inicializa en 0.0 y no se puede alterar desde la petición externa
    total: float = Field(default=0.0, init=False)

    # "para tener en cuenta cuando se necesite más seguridad"
    # Se declara, pero se oculta del constructor
    # total: float | None = Field(default=None, init=False)

    @model_validator(mode="after")
    def calcular_total(self) -> "Venta":
        """Método encagado de calcular el valor total venta"""
        self.total = self.cantidad * self.precio
        return self

    def __str__(self) -> str:
        return f"""
        Producto: {self.nombre}
        Cantidad: {self.cantidad}
        Precio: {self.precio}
        Total. {self.total}
        """
