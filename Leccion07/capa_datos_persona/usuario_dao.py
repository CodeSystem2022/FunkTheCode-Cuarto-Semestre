from capa_datos_persona.Usuario import Usuario
from capa_datos_persona.cursor_del_pool import CursorDelPool
from logger_base import log

class UsuarioDao:
    '''
    DAO -> Data acces object para la tabla de usuario
    CRUD ->Create  - read - update - delete
    '''

    _SELECT = 'SELECT * FROM usuario ORDER BY  id_usuario'
    _INSERTAR =  'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password = %s WHERE  id_usuario= %s'
    _ELIMINAR = 'DELETE FROM  usuario WHERE id_usuario =%s'

    @classmethod
    def seleccionar(cls):
         with CursorDelPool() as cursor:
             log.debug('seleccionando usuarios')
             cursor.execute(cls._SELECT)
             registros = cursor.fetchall()
             usuarios = []
             for registros in registros:
                 usuario = Usuario(registro[0], registro[1], registro[2])
                 usuarios.append(usuario)
             return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls.ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls.ELIMINAR, valores)
            return cursor.rowcount