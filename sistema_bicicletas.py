from datetime import datetime

# =====================================
# VARIABLES GLOBALES
# =====================================

clientes = []
bicicletas = []
alquileres = []

id_cliente = 1
id_bicicleta = 1

PRECIO_POR_HORA = 2000


# =====================================
# VALIDACIONES
# =====================================

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error. Debe ingresar un número.")


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto != "":
            return texto

        print("Error. No puede estar vacío.")


def pedir_dni():
    while True:

        dni = input("DNI: ")

        if dni.isdigit():
            return dni

        print("Error. El DNI debe contener solo números.")


# =====================================
# CLIENTES
# =====================================

def registrar_cliente():

    global id_cliente

    print("\n--- REGISTRAR CLIENTE ---")

    nombre = pedir_texto("Nombre: ")
    dni = pedir_dni()
    telefono = pedir_texto("Teléfono: ")

    cliente = {
        "id": id_cliente,
        "nombre": nombre,
        "dni": dni,
        "telefono": telefono
    }

    clientes.append(cliente)

    print("Cliente registrado correctamente.")

    id_cliente += 1


def mostrar_clientes():

    if len(clientes) == 0:
        print("No existen clientes.")
        return

    print("\nCLIENTES:")

    for cliente in clientes:

        print(
            f"ID: {cliente['id']} | "
            f"Nombre: {cliente['nombre']} | "
            f"DNI: {cliente['dni']}"
        )


def buscar_cliente():

    dni = pedir_dni()

    encontrado = False

    for cliente in clientes:

        if cliente["dni"] == dni:

            print("\nCLIENTE ENCONTRADO")
            print(f"ID: {cliente['id']}")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Teléfono: {cliente['telefono']}")

            encontrado = True

    if not encontrado:
        print("Cliente no encontrado.")


# =====================================
# BICICLETAS
# =====================================

def registrar_bicicleta():

    global id_bicicleta

    print("\n--- REGISTRAR BICICLETA ---")

    modelo = pedir_texto("Modelo: ")
    tipo = pedir_texto("Tipo: ")

    bicicleta = {
        "id": id_bicicleta,
        "modelo": modelo,
        "tipo": tipo,
        "disponible": True,
        "usos": 0
    }

    bicicletas.append(bicicleta)

    print("Bicicleta registrada.")

    id_bicicleta += 1


def mostrar_bicicletas():

    if len(bicicletas) == 0:
        print("No existen bicicletas.")
        return

    print("\nBICICLETAS")

    for bici in bicicletas:

        estado = "Disponible"

        if not bici["disponible"]:
            estado = "Alquilada"

        print(
            f"ID: {bici['id']} | "
            f"Modelo: {bici['modelo']} | "
            f"Tipo: {bici['tipo']} | "
            f"Estado: {estado}"
        )


# =====================================
# ALQUILERES
# =====================================

def alquilar_bicicleta():

    if len(clientes) == 0:
        print("Debe registrar clientes.")
        return

    if len(bicicletas) == 0:
        print("Debe registrar bicicletas.")
        return

    mostrar_clientes()

    id_cliente_buscar = pedir_entero(
        "Ingrese ID del cliente: "
    )

    cliente = None

    for c in clientes:

        if c["id"] == id_cliente_buscar:
            cliente = c

    if cliente is None:
        print("Cliente inexistente.")
        return

    print("\nBICICLETAS DISPONIBLES")

    disponibles = 0

    for bici in bicicletas:

        if bici["disponible"]:

            disponibles += 1

            print(
                f"ID: {bici['id']} - "
                f"{bici['modelo']}"
            )

    if disponibles == 0:
        print("No hay bicicletas disponibles.")
        return

    id_bici = pedir_entero(
        "Ingrese ID bicicleta: "
    )

    bicicleta = None

    for bici in bicicletas:

        if bici["id"] == id_bici and bici["disponible"]:
            bicicleta = bici

    if bicicleta is None:
        print("Bicicleta no disponible.")
        return

    bicicleta["disponible"] = False

    alquiler = {
        "cliente_id": cliente["id"],
        "cliente": cliente["nombre"],
        "bicicleta_id": bicicleta["id"],
        "modelo": bicicleta["modelo"],
        "inicio": datetime.now()
    }

    alquileres.append(alquiler)

    print("Alquiler registrado.")
    print("Inicio:", alquiler["inicio"])


def devolver_bicicleta():

    if len(alquileres) == 0:
        print("No existen alquileres.")
        return

    id_bici = pedir_entero(
        "ID bicicleta a devolver: "
    )

    alquiler_activo = None

    for alquiler in alquileres:

        if (
            alquiler["bicicleta_id"] == id_bici
            and "fin" not in alquiler
        ):
            alquiler_activo = alquiler

    if alquiler_activo is None:
        print("No existe alquiler activo.")
        return

    fin = datetime.now()

    alquiler_activo["fin"] = fin

    tiempo = fin - alquiler_activo["inicio"]

    horas = tiempo.total_seconds() / 3600

    if horas < 1:
        horas = 1

    importe = round(horas * PRECIO_POR_HORA, 2)

    alquiler_activo["horas"] = round(horas, 2)
    alquiler_activo["importe"] = importe

    for bici in bicicletas:

        if bici["id"] == id_bici:

            bici["disponible"] = True
            bici["usos"] += 1

    print("\nDEVOLUCIÓN EXITOSA")
    print("Horas utilizadas:", round(horas, 2))
    print("Importe a pagar: $", importe)


# =====================================
# REPORTES
# =====================================

def mostrar_alquileres():

    if len(alquileres) == 0:
        print("No existen alquileres.")
        return

    print("\nALQUILERES")

    for alquiler in alquileres:

        print("-" * 40)

        print("Cliente:", alquiler["cliente"])
        print("Bicicleta:", alquiler["modelo"])
        print("Inicio:", alquiler["inicio"])

        if "fin" in alquiler:
            print("Fin:", alquiler["fin"])
            print("Horas:", alquiler["horas"])
            print("Importe:", alquiler["importe"])
        else:
            print("Estado: ACTIVO")


def estadisticas():

    print("\n===== ESTADÍSTICAS =====")

    total_recaudado = 0

    for alquiler in alquileres:

        if "importe" in alquiler:
            total_recaudado += alquiler["importe"]

    print("Total recaudado: $", total_recaudado)

    disponibles = 0
    alquiladas = 0

    for bici in bicicletas:

        if bici["disponible"]:
            disponibles += 1
        else:
            alquiladas += 1

    print("Disponibles:", disponibles)
    print("Alquiladas:", alquiladas)

    bicicleta_top = None
    max_usos = -1

    for bici in bicicletas:

        if bici["usos"] > max_usos:
            max_usos = bici["usos"]
            bicicleta_top = bici

    if bicicleta_top is not None:

        print(
            "Bicicleta más utilizada:",
            bicicleta_top["modelo"],
            f"({max_usos} usos)"
        )

    contador_clientes = {}

    for alquiler in alquileres:

        cliente = alquiler["cliente"]

        if cliente in contador_clientes:
            contador_clientes[cliente] += 1
        else:
            contador_clientes[cliente] = 1

    mejor_cliente = None
    mayor = 0

    for nombre, cantidad in contador_clientes.items():

        if cantidad > mayor:
            mayor = cantidad
            mejor_cliente = nombre

    if mejor_cliente is not None:

        print(
            "Cliente con más alquileres:",
            mejor_cliente,
            f"({mayor} alquileres)"
        )


# =====================================
# MENÚ
# =====================================

while True:

    print("\n")
    print("=" * 40)
    print("SISTEMA DE ALQUILER DE BICICLETAS")
    print("=" * 40)

    print("1 - Registrar cliente")
    print("2 - Registrar bicicleta")
    print("3 - Alquilar bicicleta")
    print("4 - Devolver bicicleta")
    print("5 - Mostrar clientes")
    print("6 - Mostrar bicicletas")
    print("7 - Buscar cliente por DNI")
    print("8 - Mostrar alquileres")
    print("9 - Estadísticas")
    print("0 - Salir")

    opcion = pedir_entero("Opción: ")

    if opcion == 1:
        registrar_cliente()

    elif opcion == 2:
        registrar_bicicleta()

    elif opcion == 3:
        alquilar_bicicleta()

    elif opcion == 4:
        devolver_bicicleta()

    elif opcion == 5:
        mostrar_clientes()

    elif opcion == 6:
        mostrar_bicicletas()

    elif opcion == 7:
        buscar_cliente()

    elif opcion == 8:
        mostrar_alquileres()

    elif opcion == 9:
        estadisticas()

    elif opcion == 0:
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")