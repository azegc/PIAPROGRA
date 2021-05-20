class Cursos:
    def __init__(self, id_curso=5, descripcion="Desarrollo", id_empleado=5):
        self.__id_curso = id_curso
        self.__descripcion = descripcion
        self.__id_empleado = id_empleado
    def guardar(self, id_curso="5", descripcion="Educacion", id_empleado="5"):
        self.__id_curso = id_curso
        self.__descripcion = descripcion
        self.__id_empleado = id_empleado
        archivo = open("cursos.txt", 'a')
        archivo.write(id_curso)
        archivo.write("|")
        archivo.write(descripcion)
        archivo.write("|")
        archivo.write(id_empleado)
        archivo.write('\n')
        archivo.close()
        archivo = open("cursos.txt", 'r')
        imprimir = archivo.read()
        print(imprimir)
        archivo.close
    def consultar_por_id(self,id):
        self.id = id
        archivo = open("cursos.txt")
        for linea in archivo:
            datos = linea.strip().split('|')
            id_curso = datos[0]
            descripcion = datos[1]
            id_empleado = datos[2]
            if id_curso == id:
                print(id_curso,descripcion,id_empleado)
        archivo.close()