from usando_json.persistencia_gestor.gestor_cliente import GestorCliente

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

                case 0:
                    print("Saliendo del gestor de clientes")
                    break

        except ValueError:
            print("Ingrese un valor númerico o ingrese una opción válida")


if __name__ == "__main__":
    menu()
