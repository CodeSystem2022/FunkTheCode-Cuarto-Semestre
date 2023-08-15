from capa_datos_persona.usuario_dao import UsuarioDAO
from logger_base import log
opcion = None
while opcion != 5:
    print('Opciones:')
    print('1. Listar Usuarios')
    print('2. Agregar Usuario')
    print('1. Modificar Usuario')
    print('1. Eliminar Usuario')
    print('1. salir')
    opcion = int(input('digite la opcion (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('digite el nombre de usuario: ')
        password_var = input('digite su contraseña: ')
        usuario = Usuario(username = username_var, password= password_var)
        usuario_insertado = UsuarioDAO.insertar(usuario)
        log.info(f'Usuario insertado: {usuario_insertado}')
    elif opcion == 3:
        id_usuario_var = int(input('digite el id del usuario a modificar: '))
        username_var = input('digite el nombre del usuario a modificar: ')
        password_var =input('digite la contraseña del usuario a modificar ')
        usuario = usuario(id_usuario=id_usuario_var, username=username_var,password=password_var)
        usuario_actualizado= UsuarioDAO.actualizar(usuario)
        log.info(f'Ususario actualizado: {usuario_actualizado}')
    elif opcion == 4:
        id_usuario_var = int(input('digite el id del usuario a eliminar: '))
        usuario = usuario(id_usuario=id_usuario_var)
        usuario_eliminado=UsuarioDAO.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuario_eliminado}')


else:
    log.info('salimos de la aplicacion, hasta pronto!!!')