# Sistema de Alquiler de Bicicletas - TFI Algoritmos y Estructuras de Datos

def validar_entero(mensaje):
    """Solicita un número entero por consola y maneja errores si el usuario ingresa texto."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: Por favor ingrese un número positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número entero.")

def registrar_alquiler(bicicletas_disponibles, alquileres_activos):
    """Registra un nuevo alquiler si hay bicicletas disponibles."""
    if bicicletas_disponibles <= 0:
        print("\nLo sentimos, no hay bicicletas disponibles en este momento.")
        return bicicletas_disponibles
    
    print("\n--- Registrar Alquiler ---")
    dni_cliente = validar_entero("Ingrese el DNI del cliente: ")
    
    if dni_cliente in alquileres_activos:
        print("Error: Este cliente ya tiene una bicicleta en uso.")
        return bicicletas_disponibles
    
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    
    # Se guarda en el diccionario de alquileres activos
    alquileres_activos[dni_cliente] = nombre_cliente
    bicicletas_disponibles -= 1
    print(f"Alquiler registrado con éxito. Bicicletas restantes: {bicicletas_disponibles}")
    
    return bicicletas_disponibles

def finalizar_alquiler(bicicletas_disponibles, alquileres_activos, total_recaudado, total_alquileres_historicos):
    """Finaliza el uso de la bicicleta, calcula el importe y actualiza las estadísticas."""
    print("\n--- Finalizar Alquiler ---")
    if not alquileres_activos:
        print("No hay alquileres activos en el sistema.")
        return bicicletas_disponibles, total_recaudado, total_alquileres_historicos

    dni_cliente = validar_entero("Ingrese el DNI del cliente que devuelve la bicicleta: ")
    
    if dni_cliente not in alquileres_activos:
        print("Error: No se encontró un alquiler activo para ese DNI.")
        return bicicletas_disponibles, total_recaudado, total_alquileres_historicos
    
    horas_uso = validar_entero("Ingrese la cantidad de horas de uso: ")
    precio_por_hora = 1500  # Tarifa fija definida en el sistema
    importe_total = horas_uso * precio_por_hora
    
    print(f"\nResumen de la devolución:")
    print(f"Cliente: {alquileres_activos[dni_cliente]}")
    print(f"Horas utilizadas: {horas_uso}")
    print(f"Importe a abonar: ${importe_total}")
    
    # Actualización de contadores y acumuladores
    del alquileres_activos[dni_cliente]
    bicicletas_disponibles +=