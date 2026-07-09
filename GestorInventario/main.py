from GestorInventario.gestor_inventario import Inventario

inventario = Inventario()


def menu():
    print("Control de inventrio y ventas")


while True:
    print("1. Registrar producto")
    print("2. Listar producto")
    print("3. Buscar por nombre")
    print("4. Actualizar producto")
    print("5. Cambiar estado")
    print("6. Vender Producto")
    print("0. Salir")
    try:
        option = int(input("Ingrese un valor entre (1 - 6) o 0 cero para salir "))
        match option:
            case 1:
                try:
                    nombre = input("Ingrese el nombre del roducto: ")
                    stock = int(input("Ingrese las unidades del producto: "))
                    precio = float(input("Ingrese el precio del producto: "))
                    if nombre is None or stock is None or precio is None:
                        raise ValueError("Ningún campo debe estar vácio")
                    registro = inventario.registrar_producto(
                        nombre=nombre, stock=stock, precio=precio
                    )
                    if registro is False:
                        print("El producto ya existe, se sumaron los stocks")
                    else:
                        print("Producto registrado de manera exitosa")
                except ValueError as e:
                    print(e)
            case 2:
                productos = inventario.listar_productos()
                for p in productos:
                    print(p)
            case 3:
                nombre = input("Ingrese el nombre del producto que desea buscar: ")
                producto = inventario.listar_por_nombre(nombre=nombre)
                if producto is None:
                    print("El producto que busca no existe")
            case 4:
                nombre = input("Ingrese el nombre del roducto:")
                stock = int(input("Ingrese las unidades del producto: "))
                producto = inventario.actualizar_prodcuto(nombre=nombre, stock=stock)
                if producto is None:
                    print("El producto no existe en el inventario")
                if producto is True:
                    print("El prducto existe, se han agregado nuevos stocks")
            case 5:
                nombre = input(
                    "Ingrese el nombre del producto que desea modificar su estado: "
                )

                producto = inventario.cambiar_estado(nombre=nombre)
                if producto is False:
                    print("Producto disonible")
                elif producto is True:
                    print("producto agotado")
                elif producto is None:
                    print("El producto no existe")
            case 6:
                nombre = input("Ingrese el nombre del prodcuto a vender: ")
                cantidad = int(
                    input("Ingrese la cantidad que desea vender del producto: ")
                )

                producto = inventario.vender_producto(nombre=nombre, cantidad=cantidad)

                if producto is False:
                    print("No hay stocks disponibles del producto")
                if producto is True:
                    producto_precio = inventario.listar_por_nombre(
                        nombre=nombre
                    )  # sustrae el precio del objeto para calcular el valor total de la ventap
                    if producto_precio:
                        print(f"""
                            Se vendio la cantidad de {cantidad}
                            del producto {nombre}
                            por el valor de $ {cantidad * producto_precio.precio}
""")
            case 0:
                print("Saliendo del gestor ve venta e inventario...")
                break
    except ValueError:
        print("Ingrese un valor valido dentro del rango o un valor numerico")


if __name__ == "__main__":
    menu()
