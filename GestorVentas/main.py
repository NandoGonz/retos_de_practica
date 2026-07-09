"""Importamos la clase Gestor_Ventas"""

from gestor_ventas import GestorVentas
from venta import Venta


def menu():
    """Método ecncargado de controlar los datos
    ingresados por el usuario par ala gestión de las ventas"""
    gestor = GestorVentas()

    while True:
        print("#" * 70)
        print("Bienvenidos al gestor de ventas")
        print("#" * 70)
        print("1. Crear una venta")
        print("2. Listar todas las ventas")
        print("0. Salir")
        print("#" * 70)

        try:
            opcion = int(input("Ingrese la opcion a usar: "))
            match opcion:
                case 1:
                    nombre = input("Ingrese el nombre del producto: ")
                    cantidad = int(input("Ingresa la cantidad del producto a vender: "))
                    precio = float(input("Ingrese el valor del producto: "))
                    venta = Venta(nombre=nombre, cantidad=cantidad, precio=precio)
                    gestor.generar_venta(venta=venta)
                    print("Venta creada con exito")
                case 2:
                    ventas = gestor.listar_ventas()
                    for v in ventas:
                        print(v)
                case 0:
                    print("Saliendo del gestor de ventas")
                    break
        except ValueError:
            print("Ingrese un valor valido")


if __name__ == "__main__":
    menu()
