"""crear una clase vehiculo que se encargeu de mostrar la información del vehiuclo
crear una clase que se encargue de gestionar la información guardar, listar y mostrar
crear un menú por terminal para la interacción del ususario"""


class Vehiculo:
    def __init__(self, modelo: str, placa: str, marca: str):
        self.modelo = modelo
        self.placa = placa
        self.marca = marca

    def __str__(self):
        return f"""
        Modelo del vehiculo {self.modelo}
        Marca del vehiculo {self.marca}
        Placa del vehiculo {self.placa}"""


class GestorVehiculo:
    def __init__(self):
        self.vehiculos = []
        self.menu()

    def registrar_vehiculo(self, modelo: str, placa: str, marca: str):
        try:
            for v in self.vehiculos:
                if v.placa == placa:
                    raise ValueError("Ya exite un vehiculo registrado con esa placa")
            self.vehiculos.append(Vehiculo(modelo=modelo, placa=placa, marca=marca))
            print("Vehiculo registrado con exito")
        except ValueError as e:
            print(e)

    def listar_vehiculo(self):
        for i in self.vehiculos:
            print(i)

    def filtrar_por_placa(self, placa: str):
        try:
            for v in self.vehiculos:
                if v.placa == placa:
                    return f"Hay un vehiculo registrado con la placa {placa}"
            raise ValueError(f"No hay vehiculo registrado con esa placa {placa}")
        except ValueError:
            return None

    def menu(self):
        print("Control de vehiculos")
        while True:
            print("1. Registrar Vehiculo")
            print("2. Ver todos los vehiculos registrados")
            print("3. Buscar vehiculo por placa")
            print("0. Salir")
            try:
                opcion = int(input("Ingrese una opcion: "))
                match opcion:
                    case 1:
                        modelo = input("Ingrese el modelo del vehiculo: ").lower()
                        placa = input("Ingrese la placa del vehiculo: ").lower()
                        marca = input("Ingrese la marca del vehiculo: ").lower()
                        self.registrar_vehiculo(modelo=modelo, placa=placa, marca=marca)
                    case 2:
                        self.listar_vehiculo()
                    case 3:
                        placa = input(
                            "Ingrese la placa del vehiculo a buscar: "
                        ).lower()
                        filtro = self.filtrar_por_placa(placa)
                        print(filtro)
                    case 0:
                        print("Saliendo del control de vehiculos...")
                        break
            except ValueError:
                print("Ingrese una opción valida")


par = GestorVehiculo()
