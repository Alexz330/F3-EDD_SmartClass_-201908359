


class Meses:
    def __init__(self,mes, matrizTarea):
        self.mes  = mes
        self.matrizTarea = matrizTarea
      

class Node:
	def __init__(self, meses, next=None, previuous=None):
		self.meses = meses
		self.next = next
		self.previous = previuous



class Lista_Meses:

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

         

