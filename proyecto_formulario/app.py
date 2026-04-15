import json
import hashlib

#sin flask 

# 🔐 FUNCION HASH
def hash_password(password):
    # 👉 .encode() convierte el texto a bytes (requerido por hashlib)
    # 👉 sha256 crea un hash (no reversible)
    # 👉 hexdigest() lo convierte en string para poder guardarlo en JSON
    return hashlib.sha256(password.encode()).hexdigest()


# 📂 CARGAR USUARIOS
try:
    with open("usuarios.json", "r") as f:
        usuarios = json.load(f)
except:
    usuarios = {}


# 🔧 ARREGLAR USUARIOS VIEJOS (si eran string)
for u in usuarios:
    if isinstance(usuarios[u], str):
        usuarios[u] = {
            "password": hash_password(usuarios[u]),
            "edad": "",
            "email": ""
        }


# 🔁 LOOP PRINCIPAL
while True:
    print("\n1. Login")
    print("2. Registro")
    print("3. Salir")
    print("4. Eliminar usuario")

    opcion = input("Elige por Numero: ")

    # ================= LOGIN =================
    if opcion == "1":
        user = input("Usuario: ")

        if user in usuarios:

            if isinstance(usuarios[user], dict):# yaque habian stings de los usuarios pasados y ahora es edad email password todo en un {} = dict y no string
        #verifica que sea estructura correcta antes de usarla
                
                password = input("Contraseña: ")
                password_hash = hash_password(password)

                if usuarios[user]["password"] == password_hash:
                    print("✅ Login correcto")

                    if user == "admin":
                        print("👑 Bienvenido admin")
                else:
                    print("❌ Contraseña incorrecta")

            else:
                print("⚠️ Usuario en formato viejo")
        else:
            print("❌ Usuario no existe")


    # ================= REGISTRO =================
    elif opcion == "2":
        user = input("Usuario nuevo: ")

        if user in usuarios:
            print("⚠️ Ya existe")
        else:
            password = input("Nueva contraseña: ")
            edad = input("Edad: ")
            email = input("Email: ")

            usuarios[user] = {
                "password": hash_password(password),
                "edad": edad,
                "email": email
            }

            with open("usuarios.json", "w") as f:
                json.dump(usuarios, f)

            print(f"✅ Se ha registrado {user}")


    # ================= SALIR =================
    elif opcion == "3":
        break


    # ================= ELIMINAR =================
    elif opcion == "4":
        user = input("Usuario a eliminar: ")
        password = input("Confirma contraseña: ")

        if user in usuarios:

            if isinstance(usuarios[user], dict):

                password_hash = hash_password(password)

                if usuarios[user]["password"] == password_hash:
                    del usuarios[user]

                    with open("usuarios.json", "w") as f:
                        json.dump(usuarios, f)

                    print("✅ Usuario eliminado")
                else:
                    print("❌ Contraseña incorrecta")

            else:
                print("⚠️ Usuario en formato viejo")
        else:
            print("❌ Usuario no existe")
            