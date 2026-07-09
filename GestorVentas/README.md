# Gestor de ventas
Este programa gestiona la venta de un producto

# Objetivo 
Gestionar la venta de un solo producto, la finalidad de este proyectos es trabajar de forma sincronizada con el gestor de clientes para asignar una a un cliente "en el apartado de posibles mejoras se describen los cambios a realizar a fututro"
# Tecnologías utilizadas 
- Python
- Pydantic

# Estructura del proyecto 

proyecto/
|
|-- venta.py
|-- gestor_ventas.py
|__ main.py

El archivo venta.py contine se encarga de modelar los datos que se necesitan para realiar una venta y contiene el __str__ para mostrar de forma detallada la venta realizada

El archivo gestor_ventas.py se encarga de afminatrar la lógica del ejercicio 

main.py es el timon del poryecto, ya que este permite al ususario interactuar directamente con nuestro programa 

# Arquitectura 
El usuario ingresa lo sdatos desde main.py, con esa información se crea una instancia del modelo Venta.
Posteriormente, el objeto Venta se envía a GestorVentas, donde se registra y almacena para su posterios consultafg

# Forma de uso 
