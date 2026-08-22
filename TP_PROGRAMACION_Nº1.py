# TRABAJO PRACTICO DE PROGRAMACION Nº1 - BASCUÑAN BRAIAN

# EJERCICIO Nº1

# Variables utilizadas
# nombre_cliente = ""
# cantidad_productos= 0
# productos = []
# valor_producto= 0
# descuento= ""
# valor_total = 0
# valor_final = 0
# valor_ahorro = 0
# promedio_productos = 0

# Solicitud de nombre
# while True:
#    nombre_cliente = input("Ingrese nombre del cliente: ")
#    if nombre_cliente =="":
#        print("Debe ingresar un nombre para continuar")

#    elif nombre_cliente.isalpha():
#        break
#    else:
#        print("Debe ingresar solo letras")

# Solicitud cantidad final de productos
# while True:
#    cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")

#    if cantidad_productos == "":
#        print ("Debe ingresar un valor")
#    elif not cantidad_productos.isdigit():
#        print("Debe ingresar un valor numerico")
#    elif int(cantidad_productos) <= 0:
#        print("Debe ingresar un valor mayor a 0")
#    else:
#        cantidad_productos = int(cantidad_productos)
#        break

# Carga de valores
# for i in range(cantidad_productos):

#    while True:
#        valor_producto = input(f"ingrese el valor entero del producto {i+1}: ")

#        if valor_producto == "":
#            print("Debe ingresar un valor")
#        elif not valor_producto.isdigit():
#            print("Debe ingresar un valor numerico")
#        else:
#            valor_producto = int(valor_producto)
#            break

#    while True:
#        descuento = input ("¿El producto posee descuento?: S/N: ")

#        if descuento.lower() == "s":
#            break
#        elif descuento.lower() == "n":
#            break
#        else:
#            print("Debe ingresar S o N")

#    valor_total += valor_producto

# Diferenciacion por descuento
#    if descuento.lower() == "s":
#         valor_ahorro += valor_producto *0.10

# Carga a la base de deatos
#    productos.append(f"Producto {i + 1} - Precio: {valor_producto} Descuento (S/N): {descuento}")

# Calculos
# valor_final = valor_total - valor_ahorro
# promedio_productos = valor_final / cantidad_productos

# Consola
# print(f"Cliente: {nombre_cliente}")
# print(f"Cantidad de productos: {cantidad_productos}")

# for producto in productos:
#    print(producto)

# print(f"Total sin descuentos: ${valor_total}")
# print(f"Total con descuentos: ${valor_final:.2f}")
# print(f"Ahorro: ${valor_ahorro:.2f}")
# print(f"Promedio por producto: ${promedio_productos:.2f}")


# EJERCICIO Nº2

# Variables utilizadas

# usuario_correcto = "alumno"
# contraseña_correcta = "python123"
# acceso= False

# for intento in range (1,4) :
#    print(f"intento: {intento}")
#    usuario = input("Ingrese su nombre de usuario: ")
#    contraseña = input("Ingrese su contraseña: ")

#    if usuario_correcto == usuario and contraseña_correcta == contraseña:
#        print ("Acceso concedido")
#        print("")
#        acceso = True
#        break
#    else:
#        print("Credenciales invalidas")

# if acceso == False :
#    print ("Cuenta bloqueada")
# else:
#    while True:
#        print("-----MENU-----")
#        print("")
#        print("1- Estado de inscripcion")
#        print("2- Cambiar contraseña")
#        print("3- Mostrar mensaje motivacional")
#        print("4- Salir")
#        print("")

#        opcion = input ("Elegi una opcion: ")

#        if not opcion.isdigit():
#            print("Ingrese un valor numerico")
#        else:
#            opcion = int(opcion)

#            if opcion < 1 or opcion > 4:
#                print("Error opcion fuera de rango")
#            else:
#                if opcion == 1:
#                    print("INSCRIPTO")
#                elif opcion == 2:
#                    nueva_contraseña = input("Ingrese su nueva contraseña: ")

#                    if len(nueva_contraseña) < 6:
#                        print("La contraseña debe tener minimo 6 caracteres")
#                    else:
#                        confirmacion = input("confirme su contraseña nueva: ")
#                        if nueva_contraseña == confirmacion :
#                            print("Contraseña cambiada con exito")
#                            contraseña_correcta = nueva_contraseña
#                        else:
#                            print("Las contraseñas no coinciden")
#                elif opcion == 3:
#                    print("Cada pequeño paso que das te acerca a tus objetivos")
#                elif opcion == 4:
#                    break

#                print("")


# EJERCICIO Nº3

# # Variables utilizadas
# operador = ""
# lunes1 = ""
# lunes2 = ""
# lunes3 = ""
# lunes4 = ""
# martes1 = ""
# martes2 = ""
# martes3 = ""

# print("---SISTEMA CENTRAL CLINICA---")
# print("")

# while True:
#     operador = input("ingrese el nombre del operador: ")

#     if operador == "":
#         print("Debe ingresar un nombre para continuar")
#     elif operador.isalpha():
#         print("")
#         break
#     else:
#         print("El nombre debe contener solo letras")

# print(f"Bienvenido {operador}")
# # menu de seleccion
# while True:
#     print("-----MENU-----")
#     print("")
#     print("1- RESERVAR TURNO")
#     print("2- CANCELAR TURNO")
#     print("3- VER AGENDA DEL DIA")
#     print("4- VER RESUMEN GENERAL")
#     print("5- SALIR")
#     print("")

#     opcion = input("Ingrese una opcion: ")
#     # Control input ingresado
#     if opcion == "":
#         print("Debe ingresar una opcion para continuar")
#         print("")
#     elif not opcion.isdigit():
#         print("Ingrese un valor numerico")
#         print("")
#     else:
#         opcion = int(opcion)
#         if opcion < 1 or opcion > 5:
#             print("Error opcion fuera de rango")
#         # Flujo de menu

#         # OPCION 1
#         elif opcion == 1:
#             while True:
#                 print("1- LUNES")
#                 print("2- MARTES")
#                 dia = input("Selecione un dia:")

#                 if dia == "":
#                     print("Debe ingresar una opcion para continuar")
#                     print("")
#                 elif not dia.isdigit():
#                     print("Ingrese un valor numerico")
#                     print("")
#                 else:
#                     dia = int(dia)

#                     if dia < 1 or dia > 2:
#                         print("Error opcion fuera de rango")
#                     else:
#                         break

#             while True:
#                 paciente = input("Por favor ingrese el nombre del paciente: ")

#                 if paciente == "":
#                     print("Debe ingresar un nombre para continuar")
#                 elif paciente.isalpha():
#                     print("")
#                     break
#                 else:
#                     print("Debe ingresar solo letras")
#             # Verificacion y asignacion de turno
#             if dia == 1:
#                 if (
#                     paciente == lunes1
#                     or paciente == lunes2
#                     or paciente == lunes3
#                     or paciente == lunes4
#                 ):
#                     print("El paciente ya tiene u turno asignado")
#                 elif lunes1 == "":
#                     lunes1 = paciente
#                     print("paciente asignado al turno 1")
#                 elif lunes2 == "":
#                     lunes2 = paciente
#                     print("paciente asignado al turno 2")
#                 elif lunes3 == "":
#                     lunes3 = paciente
#                     print("paciente asignado al turno 3")
#                 elif lunes4 == "":
#                     lunes4 = paciente
#                     print("paciente asignado al turno 4")
#                 else:
#                     print("No hay turnos disponibles este dia")
#             else:
#                 if paciente == martes1 or paciente == martes2 or paciente == martes3:
#                     print("El paciente ya tiene u turno asignado")
#                 elif martes1 == "":
#                     martes1 = paciente
#                     print("paciente asignado al turno 1")
#                 elif martes2 == "":
#                     martes2 = paciente
#                     print("paciente asignado al turno 2")
#                 elif martes3 == "":
#                     martes3 = paciente
#                     print("paciente asignado al turno 3")
#                 else:
#                     print("No hay turnos disponibles este dia")
#         # OPCION 2
#         elif opcion == 2:
#             while True:
#                 print("1- LUNES")
#                 print("2- MARTES")
#                 dia = input("Selecione un dia:")

#                 if dia == "":
#                     print("Debe ingresar una opcion para continuar")
#                     print("")
#                 elif not dia.isdigit():
#                     print("Ingrese un valor numerico")
#                     print("")
#                 else:
#                     dia = int(dia)

#                     if dia < 1 or dia > 2:
#                         print("Error opcion fuera de rango")
#                     else:
#                         break
#             # Verificacion y cancelacion de turno
#             while True:
#                 paciente = input("Por favor ingrese el nombre del paciente: ")

#                 if paciente == "":
#                     print("Debe ingresar un nombre para continuar")
#                 elif paciente.isalpha():
#                     print("")
#                     break
#                 else:
#                     print("Debe ingresar solo letras")

#             if dia == 1:
#                 if lunes1 == paciente:
#                     lunes1 = ""
#                     print("Turno cancelado con exito")
#                 elif lunes2 == paciente:
#                     lunes2 = ""
#                     print("Turno cancelado con exito")
#                 elif lunes3 == paciente:
#                     lunes3 = ""
#                     print("Turno cancelado con exito")
#                 elif lunes4 == paciente:
#                     lunes4 = ""
#                     print("Turno cancelado con exito")
#                 else:
#                     print("El paciente no tiene turno asignado")
#             else:
#                 if martes1 == paciente:
#                     martes1 = ""
#                     print("Turno cancelado con exito")
#                 elif martes2 == paciente:
#                     martes2 = ""
#                     print("Turno cancelado con exito")
#                 elif martes3 == paciente:
#                     martes3 = ""
#                     print("Turno cancelado con exito")
#                 else:
#                     print("El paciente no tiene turno asignado")
#         # OPCION 3
#         elif opcion == 3:
#             while True:
#                 print("1- LUNES")
#                 print("2- MARTES")
#                 dia = input("Selecione un dia:")

#                 if dia == "":
#                     print("Debe ingresar una opcion para continuar")
#                     print("")
#                 elif not dia.isdigit():
#                     print("Ingrese un valor numerico")
#                     print("")
#                 else:
#                     dia = int(dia)

#                     if dia < 1 or dia > 2:
#                         print("Error opcion fuera de rango")
#                     else:
#                         break
#             if dia == 1:
#                 print("Agenda dia lunes")
#                 if lunes1 == "":
#                     print("Turno 1 libre")
#                 else:
#                     print(f"Turno 1: {lunes1}")
#                 if lunes2 == "":
#                     print("Turno 2 libre")
#                 else:
#                     print(f"Turno 2: {lunes2}")
#                 if lunes3 == "":
#                     print("Turno 3 libre")
#                 else:
#                     print(f"Turno 3: {lunes3}")
#                 if lunes4 == "":
#                     print("Turno 4 libre")
#                 else:
#                     print(f"Turno 4: {lunes4}")
#             else:
#                 print("Agenda dia martes")
#                 if martes1 == "":
#                     print("Turno 1 libre")
#                 else:
#                     print(f"Turno 1: {martes1}")
#                 if martes2 == "":
#                     print("Turno 2 libre")
#                 else:
#                     print(f"Turno 2: {martes2}")
#                 if martes3 == "":
#                     print("Turno 3 libre")
#                 else:
#                     print(f"Turno 3: {martes3}")

#         # OPCION 4
#         elif opcion == 4:
#             ocupados_lunes = 0
#             ocupados_martes = 0

#             # Contador
#             if lunes1 != "":
#                 ocupados_lunes = ocupados_lunes + 1

#             if lunes2 != "":
#                 ocupados_lunes = ocupados_lunes + 1

#             if lunes3 != "":
#                 ocupados_lunes = ocupados_lunes + 1

#             if lunes4 != "":
#                 ocupados_lunes = ocupados_lunes + 1

#             # Contador
#             if martes1 != "":
#                 ocupados_martes = ocupados_martes + 1

#             if martes2 != "":
#                 ocupados_martes = ocupados_martes + 1

#             if martes3 != "":
#                 ocupados_martes = ocupados_martes + 1

#             # Calculos de dias
#             disponibles_lunes = 4 - ocupados_lunes
#             disponibles_martes = 3 - ocupados_martes

#             # Mostrar resumen
#             print("----- RESUMEN GENERAL -----")
#             print(f"Lunes: {ocupados_lunes} ocupados - {disponibles_lunes} disponibles")
#             print(
#                 f"Martes: {ocupados_martes} ocupados - {disponibles_martes} disponibles"
#             )

#             # Moastrar resumen
#             if ocupados_lunes > ocupados_martes:
#                 print("El lunes tiene más turnos ocupados")
#             elif ocupados_martes > ocupados_lunes:
#                 print("El martes tiene más turnos ocupados")
#             else:
#                 print("Hay empate en la cantidad de turnos ocupados")
#         # OPCION 5
#         elif opcion == 5:
#             break
