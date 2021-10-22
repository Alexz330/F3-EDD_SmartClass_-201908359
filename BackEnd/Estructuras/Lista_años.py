


from Estructuras.nodeTree import node


class Años:
    def __init__(self,años, listaSemestres,listaMeses):
        self.años  = años
        self.listaSemestres = listaSemestres
        self.listaMeses = listaMeses

class Node:
	def __init__(self, año, next=None, previuous=None):
		self.año = año
		self.next = next
		self.previous = previuous



class Lista_años:

    def __init__(self) :
        self.first = None
        self.last = None
        self.size = 0
    
    def AppendFinal(self, data):
        node = Node(data)

        if self.first is None:
            self.first = node
            
        else:
            
            node.next = self.first
            self.first.previous = node
            self.first = node
    
    def AppendStart(self,data):
        cuurent = self.first
        node = Node(data)

        if self.first is None:
            self.first = node
        
        else:
            while cuurent.next is not None:
                cuurent = cuurent.next
            cuurent.next = node
            node.previous = cuurent

    def Print(self):
        current =  self.first
        while current is not None:
            print(current.data)
            current = current.next

            
    def Delete(self,data_Delete):
        current = self.first
        while current is not None:
            if current.data == data_Delete:
                current = current.next
            else:
                if current.next is not None:
                    
                    if current.next.data == data_Delete:
                        nextT = current.next
                        current.next = nextT.next
                        current.next.previous = current
                        nextT.next = None
                        print(f'se elimino el dato: {data_Delete} con exito')

                current = current.next
    def getCodigoGraphviz(self):
        aux = self.first
        nodo_data =""
        edge_data = ""
        graph = "digraph List {\nrankdir=LR;\nnode [shape = record, color=blue , style=filled, fillcolor=skyblue];\n"

        counter = 0 

        while(aux != None):
            nodo_data += "Node" + str(counter) + "[label=\"" + aux.años.año+ "\"];\n"
            if aux.previous is not None:
                edge_data += "Node" + str(counter-1) + "->Node" + str(counter) + ";\n";
                edge_data += "Node" + str(counter) + "->Node" + str(counter-1) + ";\n";
            counter+=1;
            aux = aux.next;
        graph += nodo_data;
        graph += edge_data;
        graph += "\n}";

        return graph

    def graficar(self):
        import os 
        f = open('reporteListaAños.dot', 'w', encoding='utf-8')
        f.write(self.getCodigoGraphviz())
        f.close()
        os.system('dot -Tpng reporteListaAños.dot -o reporte/reporteListaAños.png')

         

