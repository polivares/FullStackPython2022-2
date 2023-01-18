from mysqlconnection import connectToMySQL

# Crearemos una clase llamada Grupo
class Course:
    def __init__(self, data):
        self.CourseID = data['CourseID']
        self.Code = data['Code']
        self.Name = data['Name']
        # Creamos un atributo cuya funcionalidad es simplemente
        # almacenar todos aquellos estudiantes inscritos en un curso
        self.students = [] 
    
    @classmethod
    def get_students_by_course(cls, data):
        query = "select * from Course left join CourseMembership on Course.CourseID = CourseMembership.Course left join Student on CourseMembership.Student = Student.StudentID where Course.CourseID=%(CourseID)s;"
        mysql = connectToMySQL('University')
        results = mysql.query_db(query, data)
        # La variable results contiene el resultado de nuestra query COMPLETA
        # Eso quiere decir que viene la información tanto del curso puntual,
        # como de todos los estudiantes.
        
        # Primero rescataremos la información del curso.
        # Como los datos de curso están repetidos en todos los
        # registros, basta con que accedamos a la información del primer registro
        # (es decir, índice [0]). 
        # A pesar de estar entregando también la información de los estudiantes al
        # constructor del curso, solo utilizamos aquella asociada al curso accediendo
        # solo a esas llaves del diccionar.
        course = cls(results[0])
        for row_from_db in results:
            student_data={
                'StudentID': row_from_db['StudentID'],
                'FirstName': row_from_db['FirstName'],
                'LastName': row_from_db['LastName'],
            }
            # En cada iteración, a partir de lo almacenado en
            # student_data, creamos un nuevo estudiante (Student)
            # y lo agregamos dentro de la lista students definido
            # como atributo de Course
            course.students.append(Student(student_data))
        return course

# Clase de estudiantes
class Student:
    def __init__(self, data):
        self.StudentID = data['StudentID']
        self.FirstName = data['FirstName']
        self.LastName = data['LastName']

# Clase entre CourseMembership (no usada en este ejemplo, pero recomendada)
class CourseMembership:
    def __init__(self, data):
        self.Student = data['Student']
        self.Course = data['Course']

# Curso a recuperar
data = {'CourseID': 1}
# Almacenamos en la variable curso no solo un curso en particular
# sino que también aquellos estudiantes inscritos en dicho
# curso. Para acceder a los estudiantes, utilizamos
# el atributo interno "students"
curso = Course.get_students_by_course(data)
# Imprimo información del curso
print("Código del curso", curso.Code)
print("Nombre del curso", curso.Name)
print("Alumnos del curso")
for student in curso.students:
    print(student.FirstName, student.LastName)
