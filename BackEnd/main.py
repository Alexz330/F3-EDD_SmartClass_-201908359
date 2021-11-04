
from Estructuras.ArbolB.Cursos import Cursos
from analyzers.Syntactic import parser
from analyzers.Syntactic import user_list, task_list
from Estructuras.Avl import Tree_Avl
from Estructuras.Lista_años import Lista_años, Años
from Estructuras.Lista_Meses import Lista_Meses, Meses
from Estructuras.Lista_semestres import Lista_Semestre, Semestre
from Estructuras.ArbolB.ArbolB import arbolB
from Student import Student
from flask import Flask, json, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)



f = open("Estudiantes.txt", "r", encoding="utf-8")
mensaje = f.read()
f.close()
parser.parse(mensaje)

arbol = Tree_Avl()
arbolBCusrosPensum = arbolB()      

for node in user_list.iter():
    arbol.add(Student(
                int(node.Carnet),
                node.DPI,
                node.Nombre,
                node.Carrera,
                node.Correo,
                node.Password,
                node.Creditos,
                node.Edad,
                None
                )
            )


def dictStudent():

    listStudets = arbol.inorden()
    dictSudent = []
    for student in listStudets:
        aux = {
            "no_carnet": student.no_carnet,
            "DPI": student.DPI,
            "nombre": student.name,
            "carrera": student.career,
            "correo": student.email,
            "password": student.password,
            "credist": student.credits,
            "edad": student.age,
        }

        dictSudent.append(aux)
    return dictSudent


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

    print(carnet,password)

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
        




@app.route('/estudiante', methods=['PUT'])
def modificar_estudiante():
    no_carnet = request.json["carnet"]
    dpi = request.json['DPI']
    nombre =  request.json['nombre']
    carrera = request.json['carrera']
    correo =  request.json['correo']
    password = request.json['password']
    creditos = request.json['creditos']
    edad =  request.json['edad']
  
    arbol.modificar(no_carnet, arbol.root).DPI = dpi
 
    arbol.modificar(no_carnet, arbol.root).career = carrera
  
    arbol.modificar(no_carnet, arbol.root).email = correo
    
    arbol.modificar(no_carnet, arbol.root).credits = creditos
   
    arbol.modificar(no_carnet, arbol.root).age = int(edad)
    
    arbol.modificar(no_carnet, arbol.root).no_carnet = no_carnet
  
    arbol.modificar(no_carnet, arbol.root).name = nombre
   
    arbol.modificar(no_carnet, arbol.root).password = password
   
    search_student = arbol.search(no_carnet, arbol.root)

    return jsonify({
        "carnet": search_student.no_carnet,
        "DPI": search_student.DPI,
        "nombre": search_student.name,
        "carrera": search_student.career,
        "correo": search_student.email,
        "password": search_student.password,
        "credist": search_student.credits,
        "edad": search_student.age,
    }
    )

@app.route('/estudiante', methods=['DELETE'])
def elimnarEstudiante():
    no_carnet = request.json['carnet']
    arbol.eliminar(no_carnet)
    return jsonify({"estudiantes": dictStudent()})

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


#crud de cursos por estudiante y por "cursos"
@app.route('/estudiante', methods=['POST'])
def postearCursosEstudiante():
    listaEstudiante = request.json['Estudiantes']

    for estudiante in listaEstudiante:
        listaAñosCreado = Lista_años()
        if arbol.search(int(estudiante['Carnet']),arbol.root):
            temporal = arbol.search(int(estudiante['Carnet']),arbol.root).age_list.first
            while temporal is not None:
                for listaAños in estudiante["Años"]:
                    if listaAños["Año"] == temporal.año.años:
                        temporal2 = temporal.año.listaSemestres.first
                        while temporal2 != None:
                            for listaSemestres in listaAños["Semestres"]:
                                if listaSemestres["Semestre"] == temporal2.semestres.semestre:
                                    for cursos in listaSemestres["Cursos"]:
                                        Cursito = Cursos(cursos["Codigo"],cursos["Nombre"],cursos["Creditos"],cursos["Prerequisitos"],cursos["Obligatorio"])
                                        temporal2.semestres.ArbolCursos.insertarDatos(Cursito)
                                    return "si paso"
                                else:
                                    listaSemestre = Lista_Semestre()
                                    for listaSemestres2 in listaAños["Semestres"]:
                                            arbolBCursos = arbolB()
                                            for cursos in listaSemestres2['Cursos']:
                                                cursos = Cursos(int(cursos['Codigo']),cursos['Nombre'],cursos['Creditos'],cursos['Prerequisitos'],cursos['Obligatorio'])
                                                arbolBCursos.insertarDatos(cursos)
                                            semestrito = Semestre(listaSemestres2['Semestre'], arbolBCursos)
                                            listaSemestre.AppendFinal(semestrito)

                                    añito= Años(listaAños['Año'], listaSemestre, None)
                                    
                                    arbol.search(int(estudiante['Carnet']),arbol.root).age_list.AppendFinal(añito)
                                    return ('mi LOCO SE AGREGO NUEVO SEMESTRE DE CURSOS')
                        temporal2 = temporal2.next
                    else:
                       
                        listaSemestreCreado = Lista_Semestre()
                        for ListaSemestres2 in listaAños['Semestres']:
                            arbolBCursos2 = arbolB()
                            for cursos in ListaSemestres2['Cursos']:
                                cursos = Cursos(int(cursos['Codigo']),cursos['Nombre'],cursos['Creditos'],cursos['Prerequisitos'],cursos['Obligatorio'])
                                arbolBCursos2.insertarDatos(cursos)
                            semestrito2 = Semestre(ListaSemestres2['Semestre'], arbolBCursos2)
                            listaSemestreCreado.AppendFinal(semestrito2)   
                        añito= Años(listaAños['Año'], listaSemestreCreado, None)
                        
                        listaAñosCreado.AppendFinal(añito)
                        arbol.search(int(estudiante['Carnet']),arbol.root).age_list = listaAñosCreado
                        return ('mi LOCO SE AGREGO NUEVO AÑOS Y SEMESTRE DE CURSOS')  
                temporal = temporal.next
    return "mi loco si se agregaron los cursos"                

@app.route('/cursosPensum', methods=['POST'])
def postearCursos():
    cargaCursos =  request.json["Cursos"]


    for cursos in cargaCursos:
        agregarCurso = Cursos(cursos['Codigo'],cursos['Nombre'],int(cursos['Creditos']),cursos['Prerequisitos'],cursos['Obligatorio'])
        arbolBCusrosPensum.insertarDatos(agregarCurso)
    return"se agregaron los cursos exitosamente"


if __name__ == '__main__':
    app.run(debug=True, port=8080)
    dictStudent()
