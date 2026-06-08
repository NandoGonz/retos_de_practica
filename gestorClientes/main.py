from gestor_cliente import GestorCliente

gestor = GestorCliente()


def menu():
    print("Menú para gestión del cliente")

    while True:
        print("1. Regsitrar cliente")
        print("2. Actualizar cliente")
        print("3. Actualizar estado del cliente (Activar o Desactivar)")
        print("4. Listar cliente por Documento")
        print("5 Listar clientes")
        print("Ingrese 0 para salir")

        try:
            opcion = int(input("Ingrese una opcion entre (1-5) o 0 para salir: "))
            match opcion:
                case 1:
                    try:
                        nombre = input("Ingrese el nombre del cliente: ")
                        apellido = input("Ingrese el apellido del cliente: ")
                        documento = int(input("Ingrese el documento del cliente: "))
                        email = input("Ingrese el correo electronico del cliente: ")
                        direccion = input("Ingrese la dirección del cliente: ")
                        saldo = float(input("Ingrese el saldo del cliente: "))
                        campos_obligatorios = (
                            nombre,
                            apellido,
                            documento,
                            email,
                            direccion,
                            saldo,
                        )
                        if any(campo is None for campo in campos_obligatorios):
                            raise ValueError("Debe diligenciar todos los campos")
                        cliente = gestor.registrar_cliente(
                            nombre=nombre,
                            apellido=apellido,
                            documento=documento,
                            email=email,
                            direccion=direccion,
                            saldo=saldo,
                        )
                        if cliente is False:
                            raise ValueError(
                                "Existe un cliente con ese número de identificación"
                            )
                        print("Cliente registrado correctamente")
                    except ValueError as e:
                        print(e)

                case 2:
                    try:
                        documento = int(input("Ingrese el documento del cliente: "))
                        filtro = gestor.buscar_cliente_docu(n_documento=documento)
                        if filtro is None:
                            raise ValueError("El cliente no existe")
                        nombre = input("Ingrese el nuevo nombre del cliente: ")
                        apellido = input("Ingrese el nuevo apellido del cliente: ")
                        direccion = input("Ingrese la nueva dirección del cliente: ")
                        email = input("Ingrese el nuevo email del cliente: ")
                        actualizar_cliente = gestor.actualizar_cliente(
                            nombre=nombre,
                            apellido=apellido,
                            direccion=direccion,
                            email=email,
                            documento=documento,
                        )
                        if actualizar_cliente:
                            print("Cliente actualizado de manera exitosa")
                    except ValueError as e:
                        print(e)

                case 3:
                    try:
                        documento = int(
                            input("Ingresar el número de documento del cliente: ")
                        )
                        actualizar_estado_cliente = gestor.actualizar_estado(
                            documento=documento
                        )
                        if actualizar_estado_cliente is False:
                            print("Cliente inactivo")
                        elif actualizar_estado_cliente is True:
                            print("Cliente activo")
                        elif actualizar_estado_cliente is None:
                            raise ValueError("El cliente no existe")
                    except ValueError as e:
                        print(e)

                case 4:
                    documento = int(input("Ingrese el número decumento: "))
                    cliente = gestor.buscar_cliente_docu(n_documento=documento)
                    if cliente is None:
                        print("El cliente no existe")
                    print(cliente)
                    # no un try porque solo voy a mostrar un cliente

                case 5:
                    clientes = gestor.listar_clientes()
                    for c in clientes:
                        print(c)
                # no hago un try ya que solo voy a mostrar información

                case 0:
                    print("Saliendo del gestor de clientes")
                    break

        except ValueError:
            print("Ingrese un valor númerico o ingrese una opción válida")


if __name__ == "__main__":
    menu()
