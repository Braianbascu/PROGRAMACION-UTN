# EJERCICIO Nº5

while True:
    nombre = input("ingrese el nombre del gladiador: ")

    if nombre == "":
        print("Error: Solo se permiten letras")
    elif nombre.isalpha():
        print("")
        break
    else:
        print("Error: Solo se permiten letras")

print(f"Bienvenido {nombre}")
