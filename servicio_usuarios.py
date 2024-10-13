# Función para buscar un usuario por su ID
def buscar_usuario_por_id(lista_usuarios, user_id):
    for usuario in lista_usuarios:
        if usuario['id'] == user_id:
            return usuario
    return None

# Función para modificar el nombre de un usuario por su ID
def modificar_usuario_por_id(lista_usuarios, user_id, nuevo_nombre):
    usuario = buscar_usuario_por_id(lista_usuarios, user_id)
    if usuario:
        usuario['nombre'] = nuevo_nombre
        return True
    return False
