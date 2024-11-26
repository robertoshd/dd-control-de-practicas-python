import mysql.connector

class DataBase:

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'sistemapracticas'
        )

        self.cursor = self.conexion.cursor()
        self.conexion.commit()
    
    def eliminar_practica(self, id):
        cursor = self.conexion.cursor()
        consulta = "DELETE FROM practicas WHERE id_practica = {}".format(id)
        cursor.execute(consulta)
        n = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return n

    # Función para mostrar las materias en el ComboBox
    def consultaMaterias(self):
        consulta = "SELECT descripcion FROM materias"
        cursor = self.conexion.cursor()
        cursor.execute(consulta)

        # Obtener los resultados de la consulta
        resultado = cursor.fetchall()

        # Crear una lista con los resultados obtenidos
        materias = []
        for row in resultado:
            materias.append(row[0])

        return materias
    
    # Función para mostrar los docentes en el ComboBox
    def consultaDocentes(self):
        consulta = "SELECT docente FROM docentes"
        cursor = self.conexion.cursor()
        cursor.execute(consulta)

        # Obtener los resultados de la consulta
        resultado = cursor.fetchall()

        # Crear una lista con los resultados obtenidos
        materias = []
        for row in resultado:
            materias.append(row[0])

        return materias