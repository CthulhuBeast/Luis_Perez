import datetime

# cantidad de entradas disponibles
cantidad_entradas = 100

entradas_vendidas = {}  # Diccionario para almacenar el estado de las entradas (vendida o no vendida)
entradas_precios = {   # Diccionario con los precios de las entradas por tipo
    "Platinum": 120000,
    "Gold": 80000,
    "Silver": 50000
}
asistentes = []  # Lista para almacenar los datos de los asistentes

# Generar las claves de las entradas y establecerlas inicialmente como no vendidas
for i in range(1, cantidad_entradas + 1):
    entradas_vendidas[i] = False

# Función para mostrar las ubicaciones disponibles
def mostrar_ubicaciones_disponibles():
    """Función para mostrar el estado actual de las ubicaciones disponibles"""
    print("Ubicaciones disponibles:")
    for i in range(1, cantidad_entradas + 1):
        if entradas_vendidas[i]:
            print("X", end=" ")  # Entrada vendida
        else:
            print(i, end=" ")  # Entrada disponible
    print()

# Función para realizar la compra de entradas
def comprar_entradas():
    """Función para realizar la compra de entradas"""
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
    if cantidad < 1 or cantidad > 3:
        print("Cantidad inválida. Por favor, seleccione nuevamente.")
        return

    print("Seleccione las ubicaciones disponibles (ingrese el número de ubicación):")
    mostrar_ubicaciones_disponibles()

    for _ in range(cantidad):
        ubicacion = int(input())
        if ubicacion < 1 or ubicacion > cantidad_entradas:
            print("Ubicación inválida. Por favor, seleccione nuevamente.")
            return

        if entradas_vendidas[ubicacion]:
            print("Ubicación no disponible. Por favor, seleccione otra.")
            return

        entradas_vendidas[ubicacion] = True

    run_asistente = input("Ingrese el RUN del asistente (sin guiones, puntos ni dígito verificador): ")
    if not run_asistente.isdigit() or len(run_asistente) != 8:
        print("RUN inválido. Por favor, ingrese un RUN válido.")
        return

    asistentes.append((run_asistente, cantidad))
    print("La operación se ha realizado correctamente.")

# Función para mostrar el listado de asistentes ordenados por RUN
def ver_listado_asistentes():
    """Función para mostrar el listado de asistentes ordenados por RUN"""
    print("Listado de asistentes:")
    for asistente in sorted(asistentes, key=lambda x: x[0]):
        print(asistente[0])

# Función para calcular y mostrar las ganancias totales
def mostrar_ganancias_totales():
    """Función para calcular y mostrar las ganancias totales"""
    print("Ganancias totales:")
    total_ganancias = 0
    for tipo, precio in entradas_precios.items():
        cantidad = sum([asistente[1] for asistente in asistentes if asistente[1] > 0])
        ganancias = precio * cantidad
        print(f"{tipo} ${precio:,} {cantidad} = ${ganancias:,}")
        total_ganancias += ganancias
    print(f"TOTAL {cantidad_entradas} ${total_ganancias:,}")

# Función para salir del programa
def salir():
    """Función para salir del programa"""
    fecha_actual = datetime.datetime.now()
    print("Grasias por utilizar nuestro Sistema.")
    print("Atentamente: Luis Perez")
    print("Fecha:", fecha_actual.strftime("%d/%m/%Y %H:%M:%S"))
    exit()

# Menú principal
while True:
    print("== Productora Creativos.cl ==")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        comprar_entradas()
    elif opcion == "2":
        mostrar_ubicaciones_disponibles()
    elif opcion == "3":
        ver_listado_asistentes()
    elif opcion == "4":
        mostrar_ganancias_totales()
    elif opcion == "5":
        salir()
    else:
        print("Opción inválida. Por favor, seleccione nuevamente.")
