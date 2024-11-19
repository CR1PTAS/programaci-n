'''
'''
# Estructuras de datos
clientes = {}
pedidos = {}
productos = {
    1: {"nombre": "Producto A", "precio": 10},
    2: {"nombre": "Producto B", "precio": 20},
    3: {"nombre": "Producto C", "precio": 30},
}

# Función para registrar cliente
def registrar_cliente():
    print("Registro de Cliente")
    identificador = input("Ingrese un identificador único (correo o ID): ")
    if identificador in clientes:
        print("Error: El cliente ya está registrado.")
        return
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    direccion = input("Ingrese la dirección: ")
    clientes[identificador] = {"nombre": nombre, "telefono": telefono, "direccion": direccion}
    print("Cliente registrado exitosamente.")

# Función para visualizar clientes
def visualizar_clientes():
    print("Lista de Clientes Registrados:")
    for identificador, datos in clientes.items():
        print(f"ID: {identificador}, Nombre: {datos['nombre']}, Teléfono: {datos['telefono']}, Dirección: {datos['direccion']}")

# Función para realizar una compra
def realizar_compra():
    print("Realizar una Compra")
    identificador = input("Ingrese el identificador del cliente: ")
    if identificador not in clientes:
        print("Error: Cliente no encontrado.")
        return
    print("Productos disponibles:")
    for id_producto, info in productos.items():
        print(f"{id_producto}: {info['nombre']} - ${info['precio']}")
    seleccion = input("Ingrese los IDs de los productos separados por comas: ")
    ids_productos = map(int, seleccion.split(","))
    total = 0
    items = []
    for id_producto in ids_productos:
        if id_producto in productos:
            total += productos[id_producto]["precio"]
            items.append(productos[id_producto]["nombre"])
    numero_pedido = len(pedidos) + 1
    pedidos[numero_pedido] = {"cliente": identificador, "productos": items, "total": total}
    print(f"Compra realizada exitosamente. Número de pedido: {numero_pedido}")

# Función para seguimiento de compra
def seguimiento_compra():
    print("Seguimiento de Compra")
    numero_pedido = int(input("Ingrese el número de pedido: "))
    if numero_pedido not in pedidos:
        print("Error: Pedido no encontrado.")
        return
    pedido = pedidos[numero_pedido]
    cliente = clientes[pedido["cliente"]]
    print(f"Cliente: {cliente['nombre']}, Teléfono: {cliente['telefono']}, Dirección: {cliente['direccion']}")
    print(f"Productos: {', '.join(pedido['productos'])}, Total: ${pedido['total']}")

# Menú principal
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Cliente")
        print("2. Visualizar Clientes")
        print("3. Realizar Compra")
        print("4. Seguimiento de Compra")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            visualizar_clientes()
        elif opcion == "3":
            realizar_compra()
        elif opcion == "4":
            seguimiento_compra()
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()
