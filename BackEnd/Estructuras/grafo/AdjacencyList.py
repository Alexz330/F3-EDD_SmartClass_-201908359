
from List import List
from Node import  NodeGraph
from Curso import Curso


class AdjacencyList:
    def __init__(self) -> None:
        self.First =  None
        self.Last =  None
    
    def get_size(self):
        aux = self.First
        counter = 0
        while aux is not None:
            counter+=1
            aux = aux.Next
        return counter
    
    def is_empty(self):
        return self.First is None

    def exist(self,verification_number):
        aux =  self.First
        while aux is not None:
            if aux.curso.codigo == verification_number:
                return True
            aux = aux.Next
        return False

    def insert_node(self,curso):
        if not self.exist(curso.codigo):
            new_list =  List()
           
            new_node = NodeGraph(curso,new_list)
            
            if self.is_empty():
                self.Last  = new_node
                self.First =  self.Last
            else:
                self.Last.Next = new_node
                new_node.Previuos = self.Last
                self.Last = new_node
        else:
            print("el valor ya exite dentro de la lista")

    def link_graph(self,value_1, value_2):
        aux = self.First
        while aux is not None:
            if aux.curso.codigo == value_1.codigo:
                aux.list.insert_value(value_2)
                break
            aux = aux.Next
        
        # while aux is not None:
        #     if aux.number == value_2:
        #         aux.list.insert_value(value_1)
        #         break
        #     aux =  aux.Next

    def get_list(self):
        aux =  self.First
        Counter = 0 
        adjacency_list = ""
        while aux is not None:
            if not aux.list.is_empty():
                aux2 =  aux.list.First
                while aux2 is not None:
                    adjacency_list+= f'-> {str(aux2.curso.codigo)}'
                    aux2 =  aux2.Next
                    
            print(f'{str(Counter)}) {str(aux.curso.codigo)} : {adjacency_list}')
            adjacency_list = ""
            Counter +=1
               
            aux =  aux.Next
          


    def getCodigoInterno(self,cursoBuscado):         
        etiqueta= ""
        aux =  self.First
         
        while aux is not None:
            
            if not aux.list.is_empty():
                aux2 =  aux.list.First
                nodo = f"nodoMateria{str(aux.curso.nombre)} "
                etiqueta += nodo+"[label =\"<C0>|"+str(aux.curso.nombre)+"\n"+ str(aux.curso.codigo)+"|<C1>\"];\n" 

            
                
                while aux2 is not None:
                                  
                    nodo2 = f'nodoMateria{str(aux2.curso.nombre)}'
                    etiqueta += f'{nodo} -> {nodo2}\n'
                    nodo2 = ""
                
                    aux2 =  aux2.Next   

            if aux.list.is_empty():
                aux2 =  aux.list.First
                nodo = f"nodoMateria{str(aux.curso.nombre)} "
                etiqueta += nodo+"[label =\"<C0>|"+str(aux.curso.nombre)+"\n"+ str(aux.curso.codigo)+"|<C1>\"];\n" 
                while aux2 is not None:
                       
                    nodo2 = f'nodoMateria{str(aux2.number)}'
                    etiqueta += f'{nodo} -> {nodo2}\n'
                    nodo2 = ""
                    aux2 =  aux2.Next


            nodo = ""
            aux =  aux.Next 
        return etiqueta 


    def  getCodigoGraphviz(self,cursoBuscado):
        contenido = self.getCodigoInterno(cursoBuscado)
        title =  f' labelloc="t";\nlabel="Sebas HAY FEEE";'
        return "digraph grafica{\n" +"rankdir=LR;\n" +"node [shape = record, style=filled, fillcolor=seashell2];\n"+title+"\n" +contenido+"}\n";

    def graficar(self,cursoBuscado):
        import os 
        f = open('GrafoCursos.dot', 'w', encoding='utf-8')
        f.write(self.getCodigoGraphviz(cursoBuscado))
        f.close()
        os.system('dot -Tpng GrafoCursos.dot -o reporteGraph.png')



    
mate1 = Curso("mate1",101)
mate2 = Curso("mate2",103)
mate_inter1 = Curso("mateIntermedia1",107)
logica = Curso("LogicaDeSistemas",795)
mate_computo1 = Curso("MatematicaComputo1",690)
ipc1 = Curso("IPC1",770)
ipc2= Curso("IPC2",771)
lenguajes = Curso("LENGUAJES",796)
mate_computo2 = Curso("MateComputo2",962)
estructura = Curso("EstucturaDeDatos",772)

grafito = AdjacencyList()

grafito.insert_node(mate1)
grafito.insert_node(mate2)
grafito.insert_node(mate_inter1)
grafito.insert_node(logica)
grafito.insert_node(mate_computo1)
grafito.insert_node(ipc1)
grafito.insert_node(ipc2)
grafito.insert_node(lenguajes)
grafito.insert_node(mate_computo2)
grafito.insert_node(estructura)

grafito.link_graph(mate1,mate2)

grafito.link_graph(mate2,mate_inter1)
grafito.link_graph(mate2,ipc1)
grafito.link_graph(mate2,logica)
grafito.link_graph(mate2,mate_computo1)

grafito.link_graph(mate_inter1,ipc2)

grafito.link_graph(ipc1,ipc2)
grafito.link_graph(ipc1,lenguajes)
grafito.link_graph(ipc1,mate_computo2)

grafito.link_graph(mate_computo1,ipc2)
grafito.link_graph(mate_computo1,lenguajes)
grafito.link_graph(mate_computo1,mate_computo2)

grafito.link_graph(logica,ipc2)
grafito.link_graph(logica,lenguajes)
grafito.link_graph(logica,mate_computo2)

grafito.link_graph(ipc2,estructura)
grafito.link_graph(lenguajes,estructura)
grafito.link_graph(mate_computo2,estructura)



grafito.get_list()
grafito.graficar(962)

