import json

# Cargar los usuarios desde un archivo JSON
def cargar_datos_usuarios():
    try:
        with open('usuarios.json', 'r') as archivo:
            return json.load(archivo)['usuarios']
    except FileNotFoundError:
        print("Archivo no encontrado, asegúrate de que 'usuarios.json' exista.")
        return []

# Guardar los usuarios en el archivo JSON
def guardar_datos_usuarios(lista_usuarios):
    with open('usuarios.json', 'w') as archivo:
        json.dump({"usuarios": lista_usuarios}, archivo, indent=4)

# Registrar un nuevo usuario
def registrar_usuario(nombre, clave):
    usuarios = cargar_datos_usuarios()
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": nombre,
        "clave": clave
    }
    usuarios.append(nuevo_usuario)
    guardar_datos_usuarios(usuarios)
    print("Usuario registrado exitosamente.")

# Autenticar usuario
def autenticar_usuario(nombre, clave):
    usuarios = cargar_datos_usuarios()
    for usuario in usuarios:
        if usuario['nombre'] == nombre and usuario['clave'] == clave:
            return True, usuario
    return False, None
