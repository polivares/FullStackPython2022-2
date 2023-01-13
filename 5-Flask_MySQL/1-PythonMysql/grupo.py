from sqlite3 import connect
from unittest import result
from mysqlconnection import connectToMySQL

# Crearemos una clase llamada Grupo
class Grupo:
    def __init__(self, data):
        # Tenemos un atributo por cada columna de nuestra
        # tabla "grupo"
        self.idGrupo = data['idGrupo']
        self.nombre_grupo = data['nombre_grupo']
        self.descripcion_grupo = data['descripcion_grupo']

    # Decorador classmethod indica que el método puede ser llamado sin instanciar la clase
    # (es decir, sin un objeto / Grupo.get_all())
    @classmethod
    def get_all(cls):
        # El método get_all se encargará de entregar información 
        # de todos los grupos presentes en la tabla "grupo"
        # Pasos para escribir esta interacción son los siguientes:
        
        # 1) Escribimos la query asociada con nuestra interacción
        query = "select * from grupo;"
        # 2) Nos conectamos con la BD para ejecutar luego nuestra 
        # query
        mysql = connectToMySQL('curso') # La conexión queda en variable 'mysql'
        # 3) Una vez conectados, ejecutamos nuestra query en la BD
        # El resultado de dicha query se almacena en la variable results
        results = mysql.query_db(query) # Conexión a la base de datos
        print("Contenido de results", results)
        grupos = []
        for result in results:
            grupo = cls(result) # cls() transforma los resultados en instancias de la clase Grupo
            grupos.append(grupo)
        return grupos
    
    @classmethod
    def get(cls, nombre_grupo):
        # Este método solo va a retornar un único grupo, dependiendo
        # de su nombre_grupo
        # 1) Creamos nuestra query, dejando pendiente el nombre_grupo como condición
        query = "select * from grupo where nombre_grupo = %(nombre_grupo)s;"
        # 2) Creamos un diccionar que tendrá la informción del nombre_grupo
        data = {'nombre_grupo': nombre_grupo}
        # 3) Creamos la conexión con la BD curso
        mysql = connectToMySQL('curso')
        # 4) Ejecutamos la query junto con la condición almacenada en
        # la variable diccionario data
        result = mysql.query_db(query, data)
        if len(result) > 0: # Verificamos que venga algún grupo
            return cls(result[0]) # Tomamos el primer resultado y lo convertimos a Grupo
        else:
            return None

    @classmethod
    def save(cls, data):
        # Dentro de la variable data, a diferencia del caso anterior
        # ya viene el diccionario de datos armado. 
        # Esto lo puedes decidir en cada caso a tu conveniencia.
        query = "insert into grupo (nombre_grupo, descripcion_grupo) values (%(nombre_grupo)s, %(descripcion_grupo)s);"
        mysql = connectToMySQL('curso')
        mysql.query_db(query, data)
        return cls.get(data['nombre_grupo'])

