from pydantic import BaseModel


class Usuario(BaseModel):
    nombre: str
    edad: int


usuario = Usuario(nombre="Luis", edad=20)
print(usuario)
