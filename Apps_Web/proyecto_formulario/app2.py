from flask import Flask, request, render_template 
import json
import hashlib

app = Flask(__name__)

# 🔐 HASH
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# 📂 CARGAR USUARIOS
def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as f:
            return json.load(f)
    except:
        return {}

# 💾 GUARDAR
def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f)

# 🏠 HOME
@app.route("/")
def home():
    return render_template("login.html")

# 🔐 LOGIN
@app.route("/login", methods=["POST"])
def login():
    usuarios = cargar_usuarios()

    user = request.form["user"]
    password = request.form["password"]
    password_hash = hash_password(password)

    if user in usuarios:
        if usuarios[user]["password"] == password_hash:
            return f"✅ Bienvenido {user}"
        else:
            return "❌ Contraseña incorrecta"
    else:
        return "❌ Usuario no existe"

# 🆕 REGISTRO

@app.route("/register")
def register_page():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    usuarios = cargar_usuarios()

    user = request.form["user"]
    password = request.form["password"]

    if user in usuarios:
        return "⚠️ Usuario ya existe"

    usuarios[user] = {
        "password": hash_password(password),
        "edad": "",
        "email": ""
    }

    guardar_usuarios(usuarios)
    from flask import redirect, url_for
    return f"✅ Usuario {user} creado: ir  a login " ,  redirect(url_for("home"))
    #return f'Usuario creado. <a href="/">Ir a login</a>' mas facil y manual
# ▶️ RUN SOLO UNA VEZ
if __name__ == "__main__":
    app.run(debug=True)