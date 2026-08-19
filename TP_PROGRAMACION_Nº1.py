#TRABAJO PRACTICO DE PROGRAMACION Nº1 - BASCUÑAN BRAIAN 

#EJERCICIO Nº1

#Variables utilizadas
#nombre_cliente = ""
#cantidad_productos= 0
#productos = []
#valor_producto= 0
#descuento= ""
#valor_total = 0
#valor_final = 0
#valor_ahorro = 0
#promedio_productos = 0

#Solicitud de nombre
#while True: 
#    nombre_cliente = input("Ingrese nombre del cliente: ")
#    if nombre_cliente =="":
#        print("Debe ingresar un nombre para continuar")

#    elif nombre_cliente.isalpha():
#        break
#    else:
#        print("Debe ingresar solo letras")

#Solicitud cantidad final de productos
#while True: 
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

#Carga de valores
#for i in range(cantidad_productos):
   
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

#Diferenciacion por descuento
#    if descuento.lower() == "s":
#         valor_ahorro += valor_producto *0.10

#Carga a la base de deatos
#    productos.append(f"Producto {i + 1} - Precio: {valor_producto} Descuento (S/N): {descuento}")

#Calculos
#valor_final = valor_total - valor_ahorro
#promedio_productos = valor_final / cantidad_productos

#Consola
#print(f"Cliente: {nombre_cliente}")
#print(f"Cantidad de productos: {cantidad_productos}")

#for producto in productos:
#    print(producto)

#print(f"Total sin descuentos: ${valor_total}")
#print(f"Total con descuentos: ${valor_final:.2f}")
#print(f"Ahorro: ${valor_ahorro:.2f}")
#print(f"Promedio por producto: ${promedio_productos:.2f}")



# EJERCICIO Nº2

#Variables utilizadas

#usuario_correcto = "alumno"
#contraseña_correcta = "python123"
#acceso= False

#for intento in range (1,4) :
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

#if acceso == False :
#    print ("Cuenta bloqueada")
#else:
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


#EJERCICIO Nº3

#Variables utilizadas

operador = ""
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

print("---SISTEMA CENTRAL CLINICA---")
print("")

while True:
    operador = input("ingrese el nombre del operador: ")

    if operador == "":
        print ("Debe ingresar un nombre para continuar")
    elif operador.isalpha():
        print("")
        break
    else:
        print("El nombre debe contener solo letras")

print(f"Bienvenido {operador}")

while True:
    print("-----MENU-----")
    print("")
    print("1- RESERVAR TURNO")
    print("2- CANCELAR TURNO")
    print("3- VER AGENDA DEL DIA")
    print("4- VER RESUMEN GENERAL")
    print("5- SALIR")
    print("")

    opcion = input("Ingrese una opcion: ")

    if opcion == "":
        print ("Debe ingresar una opcion para continuar")
        print("")
    elif not opcion.isdigit():
        print("Ingrese un valor numerico")
        print("")
    else:
        opcion = int(opcion)

        if opcion < 1 or opcion > 5:
            print("Error opcion fuera de rango")
        elif opcion == 1:
            while True:
                print("1- LUNES")
                print("2- MARTES")
                dia = input("Selecione un dia:")

                if dia == "":
                    print ("Debe ingresar una opcion para continuar")
                    print("")
                elif not dia.isdigit():
                    print("Ingrese un valor numerico")
                    print("")
                else:
                    dia = int(dia)
                
                    if dia < 1 or dia > 2:
                        print("Error opcion fuera de rango")
        elif opcion == 2:
            print("opcion 2")
        elif opcion == 3:
            print("opcion 3")
        elif opcion == 4:
            print("opcion 4")
        elif opcion ==5:
            break