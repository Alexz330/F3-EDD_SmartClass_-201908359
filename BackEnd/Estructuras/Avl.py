
from Estructuras.nodeTree import node


class Tree_Avl:

    def __init__(self):

        self.root = None

    def maximun(self, value1, value2):
        if value1 > value2:
            return value1
        else:
            return value2


    def get_height(self, node):
        if node is not None:
            return node.height
        return -1

    def add(self, student):
        self.root = self.add_intern(student, self.root)

    def add_intern(self, student, root):

        if root is None:
            return node(student)
        else:

            if student.no_carnet < root.student.no_carnet:
                root.left = self.add_intern(student, root.left)

                if self.get_height(root.right) - self.get_height(root.left) == -2:

                    if student.no_carnet < root.left.student.no_carnet:
                        root = self.rotation_left(root)

                    else:
                        root = self.rotation_right_left(root)

            elif student.no_carnet > root.student.no_carnet:
                root.right = self.add_intern(student, root.right)

                if self.get_height(root.right) - self.get_height(root.left) == 2:

                    if student.no_carnet > root.right.student.no_carnet:
                        root = self.rotation_right(root)

                    else:
                        root = self.rotation_left_right(root)
            else:
                root.student = student
        root.height = self.maximun(self.get_height(root.left), self.get_height(root.right)) + 1\

        return root

    def rotation_left(self, node):

        auxiliar = node.left
        node.left = auxiliar.right
        auxiliar.right = node
        node.height = self.maximun(self.get_height(node.left), self.get_height(node.right)) + 1
        auxiliar.height = self.maximun(self.get_height(auxiliar.left), self.get_height(auxiliar.right)) + 1

        return auxiliar

    def rotation_right(self, node):

        auxiliar = node.right
        node.right = auxiliar.left
        auxiliar.left = node
        node.height = self.maximun(self.get_height(node.left), self.get_height(node.right)) + 1
        auxiliar.height = self.maximun(self.get_height(auxiliar.left), self.get_height(auxiliar.right)) + 1

        return auxiliar

    def rotation_right_left(self, node):

        node.left = self.rotation_right(node.left)
        return self.rotation_left(node)

    def rotation_left_right(self, node):

        node.right = self.rotation_left(node.right)
        return self.rotation_right(node)

    def preorden(self):
        self.preorden_intern(self.root)

    def preorden_intern(self, root):

        if root is not None:
            print(root.student.name)
            self.preorden_intern(root.left)
            self.preorden_intern(root.right)

    def inorden(self):
        lista = []
        self.inorden_intern(self.root, lista)
        return lista

    def inorden_intern(self, root, lista):
        if root is not None:
            self.inorden_intern(root.left, lista)
            self.inorden_intern(root.right, lista)
            lista.append(root.student)
            print(root.student.name)

    def search(self, no_carnet, root):
        if root is None:
            return None
        elif no_carnet > root.student.no_carnet:
            return self.search(no_carnet, root.right)
        elif no_carnet < root.student.no_carnet:
            return self.search(no_carnet, root.left)
        else:
            return root.student




    def  eliminar(self,carnet):
        self._eliminar(carnet,self.root,None)
        self.balancear()

    def _eliminar(self,carnet, temporal, anterior):
        
        if carnet == temporal.student.no_carnet:
            if (temporal.right is None) and (temporal.left is None):
                if anterior.right == temporal:
                    anterior.right = None
                elif anterior.left == temporal:
                    anterior.left = None

            elif temporal.left is not None:
                self._encontrarReemplazo(temporal, temporal.left, anterior)
                
            elif (temporal.left is None) and (temporal.right is not None):

                if anterior.right == temporal:

                    anterior.right = temporal.right
                    temporal = None

                elif anterior.left == temporal:

                    anterior.left = temporal.right
                    temporal = None

        if temporal is not None:
            if temporal.left is not None:
                if carnet <= temporal.left.student.no_carnet:
                    self._eliminar(carnet, temporal.left, temporal)

                if temporal.right is not None:
                    if carnet >= temporal.right.student.no_carnet:
                        self._eliminar(carnet, temporal.right, temporal)       

    def _encontrarReemplazo(self, tempEliminar, temporal, anteriorValor):

        aux = temporal
        anteriorAux = None
        encicla = False

        while aux.right is not None:
            encicla = True
            anteriorAux = aux
            aux =  aux.right

        if aux.left is not None:
            anteriorAux.right = aux.left

        elif encicla == True:
            anteriorAux.right = None

        elif encicla == False:
            if tempEliminar.left == temporal:
                tempEliminar.left = temporal.left

        if anteriorValor.right == tempEliminar:
            anteriorValor.right.student.no_carnet =aux.student.no_carnet

        elif anteriorValor.left ==tempEliminar:
            anteriorValor.left.student.no_carnet =aux.student.no_carnet

        aux = None
    
    def balancear(self):
        self.balancearAlturas(self.root)
        self.root = self._balancear(self.root)

    def _balancear(self, temporal):
        if(temporal.left is None):
            return temporal
        elif temporal.right == None:
            return temporal
        else:
            temporal.left = self._balancear(temporal.left)
            if ((self.get_height(temporal.left) - self.get_height(temporal.right)) == 2):
                if temporal.left.right is None:
                    temporal = self.rotation_left(temporal)
                else:
                    temporal = self.rotation_left_right(temporal)
            temporal.right = self._balancear(temporal.right)
            if((self.get_height(temporal.right) - self.get_height(temporal.left) == 2)):
                if temporal.right.left == None:
                    temporal = self.rotation_right(temporal)
                else:
                    temporal = self.rotation_right_left(temporal)

        al_der = self.get_height(temporal.right)
        al_izq =  self.get_height(temporal.left)
        temporal.height = self.maximun(al_der,al_izq) + 1
        return temporal       


    def balancearAlturas (self, temporal):
        if temporal.left is not None:
            self.balancearAlturas(temporal.left)
        elif temporal.right is not None:
            self.balancearAlturas(temporal.right)
        temporal.height = self.maximun(self.get_height(temporal.right), self.get_height(temporal.left)) + 1
    
    def graficar(self):
        import os 
        f = open('reportes/reporteAvl.dot', 'w', encoding='utf-8')
        f.write(self.root.getCodigoGraphviz())
        f.close()
        os.system('dot -Tsvg reportes/reporteAvl.dot -o reportes/reporteAvl.svg')








# alexis  = Student(201908546,12124123,"alexis l","engenier","alexislc@gfka.com",1232,2, 231,None)
# alexis2  = Student(201906576,12124123,"alexis c","engenier","alexislc@gfka.com",1232,2, 231,None)
# alexis3  = Student(201908566,12124123,"alexis b","engenier","alexislc@gfka.com",1232,2, 231,None)
# alexis4  = Student(201903333,12124123,"alexis 2","engenier","alexislc@gfka.com",1232,2, 231,None)
# alexis5  = Student(201908767,12124123,"alexis 5","engenier","alexislc@gfka.com",1232,2, 231,None)
# alexis6  = Student(201965434,12124123,"alexis 5","engenier","alexislc@gfka.com",1232,2, 231,None)

# avlesito = Tree_Avl()

# avlesito.add(alexis)
# avlesito.add(alexis2)
# avlesito.add(alexis3)
# avlesito.add(alexis4)
# avlesito.add(alexis5)
# avlesito.add(alexis6)


# avlesito.preorden()

