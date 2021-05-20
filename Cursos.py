class Cursos:
    def __init__(self, id_curso=5, descripcion="Desarrollo", id_empleado=5):
        self.__id_curso = id_curso
        self.__descripcion = descripcion
        self.__id_empleado = id_empleado
    def guardar(self, id_curso="5", descripcion="Educacion", id_empleado="5"):
        self.__id_curso = id_curso
        self.__descripcion = descripcion
        self.__id_empleado = id_empleado