
from Estructuras.ArbolB.Cursos import Cursos
from Estructuras.Avl import Tree_Avl
from Estructuras.Lista_años import Lista_años, Años
from Estructuras.Lista_Meses import Lista_Meses, Meses
from Estructuras.Lista_semestres import Lista_Semestre, Semestre
from Estructuras.ArbolB.ArbolB import arbolB
from Estructuras.HashTable.HashTable import HashTable, apunte
from Estructuras.grafo.AdjacencyList import AdjacencyList
from Estructuras.grafo.Curso import Curso
from Student import Student
from flask import Flask, json, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)



arbol = Tree_Avl()
arbolBCusrosPensum = arbolB()      
TablaApuntes = HashTable()
grafoPensum = AdjacencyList()

#endPoints para apuntes
@app.route("/apuntesAgregar", methods=['POST'])
def agregarApunte():
    title = request.json['Título']
    content = request.json['Contenido']
    carnet =  request.json['carnet']
    apuntesito = apunte(title,content)
    print(title)
    TablaApuntes.add(int(carnet),apuntesito)
    TablaApuntes.graficar()
    return f"se agrego aputene a la tablaHash"


@app.route("/ObtenerApuntes", methods=['GET',"POST"])
def obtenerApuntes():
    carnet =  request.json['carnet']
    print(carnet)
    apunesUsuario = TablaApuntes.get(int(carnet))
    return jsonify(apunesUsuario)

@app.route("/reporteTabla",methods=["GET"])
def reporteTabla():
    TablaApuntes.graficar()
    return jsonify({
        "ruta":'apuntes.png'
    })

#endPoins para pensum
@app.route("/agregarPensum", methods=["POST"])
def agregarPensum():
    pensum = request.json['pensum']
    
    for curso in pensum:
        curisito = Curso(curso["Nombre"],curso["Codigo"])
        grafoPensum.insert_node(curisito)
        
        Lista_pre = curso["Prerequisitos"].split(",")
        
        for pre in Lista_pre:
            grafoPensum.link_graph(curso["Codigo"],pre)
    grafoPensum.graficar()
    
    return "pensun agregado"

@app.route("/carga", methods=['POST'])
def cargar():

    ruta = request.json['path']
    tipo = request.json['tipo']
    
    if tipo == "estudiante":
      
        with open(ruta  ,  encoding="utf-8") as file:
            data = json.load(file)
            for dato in data['Estudiantes']:
              if arbol.search(int(dato['Carnet']),arbol.root) is not None:
               
                listaAñitos = Lista_años()
                for año in dato['Años']:
                    listitaSemestre = Lista_Semestre()
                    for semestres in año["Semestres"]:
                        arbolBCursos = arbolB()
                        for cursos in semestres['Cursos']:
                            cursos = Cursos(int(cursos['Codigo']),cursos['Nombre'],cursos['Creditos'],cursos['Prerequisitos'],cursos['Obligatorio'])
                            arbolBCursos.insertarDatos(cursos)
                        semestrito = Semestre(semestres['Semestre'], arbolBCursos)
                        listitaSemestre.AppendFinal(semestrito)
                    añito= Años(año['Año'], listitaSemestre, None)
                    listaAñitos.AppendFinal(añito)
                arbol.search(int(dato['Carnet']),arbol.root).age_list = listaAñitos
                print(arbol.search(int(dato['Carnet']),arbol.root).name)

    if tipo == "curso":
         with open(ruta  ,  encoding="utf-8") as file:
            data = json.load(file)

            for cursos in data['Cursos']:
                cursitos =  Cursos(cursos['Codigo'],cursos['Nombre'],int(cursos['Creditos']),cursos['Prerequisitos'],cursos['Obligatorio'])
                arbolBCusrosPensum.insertarDatos(cursitos)
                print('_______cursos__________')
                print(int(cursos['Codigo']),cursos['Nombre'],int(cursos['Creditos']),cursos['Prerequisitos'],cursos['Obligatorio'])


        
    return "mi loco ya se cargaron los estudiantes"
        

@app.route('/reporte', methods=['GET'])
def reporte():
    tipo = request.json["tipo"]
  
    if tipo == 0:
        arbol.graficar()
   
    if tipo == 3:
        arbolBCusrosPensum.graficar()
    if tipo == 4:
        cartnet = request.json["carnet"]
        año = request.json['año']
        semestre = request.json['semestre']
        if arbol.search(cartnet,arbol.root) is not None:
            temporal = arbol.search(cartnet,arbol.root).age_list.first
            while temporal != None:
                if año == temporal.año.años:
                    temporal2 = temporal.año.listaSemestres.first
                    while temporal2 != None:
                        if semestre == temporal2.semestres.semestre:
                            temporal2.semestres.ArbolCursos.graficar()
                            return "si paso"
                        temporal2 = temporal2.next
                temporal = temporal.next

    return "mi loco su reporte se ha realizdo con exito"

# Crud de estudiantes mi loco, guapo el que lo lea

@app.route('/estudiante', methods=['GET','POST'])
def Login():
    carnet =  request.json['carnet']
    password =  request.json['password'] 

    if carnet == "admin" and password == "admin":
             return jsonify({
                "carnet": carnet,
                "nombre": "admin",
                "userValided":True,
                "admin":True
                }
            )
   

    search_student = arbol.search(int(carnet), arbol.root)
   
    if(search_student is not None):
        if((search_student.no_carnet ==  int(carnet))  & (search_student.password == password)):
            print("logueado")
            return jsonify({
                "carnet": search_student.no_carnet,
                "DPI": search_student.DPI,
                "nombre": search_student.name,
                "carrera": search_student.career,
                "correo": search_student.email,
                "admin":False,
                "credist": search_student.credits,
                "edad": search_student.age,
                "userValided":True
                }
            )
        elif(search_student.password != password):
            return jsonify({
                "mesagge": "Contraseña o usuario incorrecto",
                "logueado":False
            })
       


    elif( search_student is None):
        print("NO se encontro usuario")
        return jsonify({
            "mesagge": "no se encontro usuario",
             "logueado":False
        })
        


@app.route('/agregarEstudiante', methods=['POST'])
def postEstudiante():
    

    no_carnet = request.json['carnet']
    DPI = request.json['dpi']
    nombre = request.json["nombre"]
    carrera = request.json["carrera"]
    correo = request.json["correo"]
    password = request.json["password"]
    edad = request.json["edad"]

    estudiante = Student(int(no_carnet), DPI, nombre, carrera,
                         correo, password, None, edad, None)
    arbol.add(estudiante)

 
    return f"se agrego el usuario {nombre}"


@app.route("/cargaMasivaEstudiantes", methods=['POST'])
def cargaEstudiantes():
    Estudiantes  =  request.json["estudiantes"]
    for estudiante in Estudiantes:
        estudiante_carga = Student(int(estudiante["carnet"]), estudiante["DPI"],estudiante["nombre"],estudiante["carrera"],estudiante["correo"],estudiante["password"],None,estudiante["edad"],None)
        arbol.add(estudiante_carga)
    
    return "carga de estudiantes realizada"


#enpoint para carga masiva de cursos para estudiantes

#agregarCurso 
@app.route("/cargaMasivaCursos",methods=["POST"])
def cargaCursosPorEstudiante():
  

    cursosEstudiate = request.json["Estudiantes"]
    print(cursosEstudiate)
    for dato in cursosEstudiate:
            if arbol.search(int(dato['Carnet']),arbol.root) is not None:
                listaAñitos = Lista_años()
                for año in dato['Años']:
                    listitaSemestre = Lista_Semestre()
                    for semestres in año["Semestres"]:
                        arbolBCursos = arbolB()
                        for cursos in semestres['Cursos']:
                            cursos = Cursos(int(cursos['Codigo']),cursos['Nombre'],cursos['Creditos'],cursos['Prerequisitos'],cursos['Obligatorio'])
                            arbolBCursos.insertarDatos(cursos)
                        semestrito = Semestre(semestres['Semestre'], arbolBCursos)
                        listitaSemestre.AppendFinal(semestrito)
                    añito= Años(año['Año'], listitaSemestre, None)
                    listaAñitos.AppendFinal(añito)
                arbol.search(int(dato['Carnet']),arbol.root).age_list = listaAñitos
                # estudiante_cursos = arbol.search(int(dato['Carnet']),arbol.root)
                # print(estudiante_cursos)
                # #arbol.search(int(dato['Carnet']),arbol.root).age_list.listaSemestres.ArbolCursos.graficar()
    return "Proceso terminado"


#enpoint para agregar curso por estudiante
@app.route('/agregarcurso',methods=["POST"])
def agregarCurso():
    carnet_de_estudiante = request.json["carnet"]
    estudiante  = arbol.search(int(carnet_de_estudiante), arbol.root)
    Curso_codigo = request.json['Codigo']
    Curso_nombre = request.json['Nombre'] 
    Curso_creditos = request.json['Creditos']
    Curso_Prerequisitos = request.json['Prerequisitos']
    Curso_Obligatorio = request.json['Obligatorio']
    curso = Cursos(int(Curso_codigo),Curso_nombre,Curso_creditos,Curso_Prerequisitos,Curso_Obligatorio)
    
    cartnet = request.json["carnet"]
    año = request.json['año']
    semestre = request.json['semestre']
    if estudiante is not None:
            temporal = arbol.search(cartnet,arbol.root).age_list.first
            while temporal != None:
                if año == temporal.año.años:
                    temporal2 = temporal.año.listaSemestres.first
                    while temporal2 != None:
                        if semestre == temporal2.semestres.semestre:
                            temporal2.semestres.ArbolCursos.insertarDatos(curso)
                            temporal2.semestres.ArbolCursos.graficar()
                            print("se agrego curso")
                            return "Se agrego curso "
                        temporal2 = temporal2.next
                temporal = temporal.next
#enpoints para generar reportes

@app.route("/reporteEstudiantes",methods=["GET"])
def reportesEstudiantes():
    arbol.graficar()
    return jsonify({
        "ruta":"BackEnd/reportes/resportes.svg"
    })

@app.route("/reporteCursos",methods=["GET","POST"])
def reporteEstudiantesCurso():
    cartnet = request.json["carnet"]
    año = request.json['año']
    semestre = request.json['semestre']
    print(cartnet,año,semestre)
    if arbol.search(int(cartnet),arbol.root) is not None:
            
            temporal = arbol.search(int(cartnet),arbol.root).age_list.first
            while temporal != None:
                if año == temporal.año.años:
                    temporal2 = temporal.año.listaSemestres.first
                    while temporal2 != None:
                        if semestre == temporal2.semestres.semestre:
                            print("hola")
                            temporal2.semestres.ArbolCursos.graficar()
                            return "si paso"
                        temporal2 = temporal2.next
                temporal = temporal.next   
    return jsonify({
        "ruta":"BackEnd/reportes/ReportePensum.png  "
    })




if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
