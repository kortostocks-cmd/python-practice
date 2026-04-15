import json

try:
    with open("usuarios.json", "r") as f:
        usuarios = json.load(f)
except:
    usuarios = {}

while True:
    print("\n1. Login")
    print("2. Registro")
    print("3. Salir")

    opcion = input("Elige por Numero: ")

    if opcion == "1":
        user = input("Usuario: ")
        password = input("Contraseña: ")

        if user in usuarios:
            if usuarios[user] == password:
                print("Login correcto")
            else:
                print("contraseña incorrecta")
        else:
            print("Usuario no existe")

    elif opcion == "2":
        user = input("Nuevo usuario: ")

        if user in usuarios:
            print("Ya existe")
        else:
            password = input("Nueva contraseña: ")
            usuarios[user] = password

            with open("usuarios2.json", "w") as f:
                json.dump(usuarios, f)

    elif opcion == "3":
        break