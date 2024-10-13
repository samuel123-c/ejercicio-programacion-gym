from gestor_usuarios import cargar_datos_usuarios, registrar_usuario, autenticar_usuario, guardar_datos_usuarios
from servicio_usuarios import buscar_usuario_por_id, modificar_usuario_por_id
from usuarios_controlador import desplegar_informacion_usuario

# Solicitar credenciales
def pedir_credenciales():
    nombre = input("Ingresa tu nombre de usuario: ")
    clave = input("Ingresa tu clave: ")
    return nombre, clave

# Registrar un nuevo usuario
def registro():
    nombre = input("Ingresa un nuevo nombre de usuario: ")
    clave = input("Ingresa una clave: ")
    registrar_usuario(nombre, clave)

# Consultar un usuario por ID
def consultar_usuario_por_id():
    user_id = int(input("Ingresa el ID del usuario que deseas consultar: "))
    usuarios = cargar_datos_usuarios()
    usuario = buscar_usuario_por_id(usuarios, user_id)
    if usuario:
        desplegar_informacion_usuario(usuario)
    else:
        print("Usuario no encontrado.")

# Modificar un usuario por ID
def modificar_usuario():
    user_id = int(input("Ingresa el ID del usuario que deseas modificar: "))
    nuevo_nombre = input("Ingresa el nuevo nombre: ")
    usuarios = cargar_datos_usuarios()
    if modificar_usuario_por_id(usuarios, user_id, nuevo_nombre):
        guardar_datos_usuarios(usuarios)
        print("Usuario modificado exitosamente.")
    else:
        print("Usuario no encontrado.")

# Función principal
def main():
    while True:
        print("\n--- Menú ---")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Consultar usuario por ID")
        print("4. Modificar usuario por ID")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre, clave = pedir_credenciales()
            autenticado, usuario = autenticar_usuario(nombre, clave)
            if autenticado:
                print(f"¡Bienvenido {usuario['nombre']}!")
            else:
                print("Nombre de usuario o clave incorrectos.")
        
        elif opcion == "2":
            registro()

        elif opcion == "3":
            consultar_usuario_por_id()

        elif opcion == "4":
            modificar_usuario()

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, por favor selecciona una opción correcta.")

if __name__ == "__main__":
    main()
