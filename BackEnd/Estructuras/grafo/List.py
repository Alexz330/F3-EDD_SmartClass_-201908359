from Node import Node

class List:
    def __init__(self):
        self.First = None
        self.Last = None
    
    def get_size(self):
        aux =  self.First
        counter =  0 
        while aux is not None:
            counter+=1
            aux  = aux.Next 

        return counter
    
    def is_empty(self):
        return self.First is None

    def get_list(self):
        aux =  self.First 
        result_list = []
        while aux is not None:
            result_list.append(aux.curso)
            aux =  aux.Next
        return result_list

    def insert_value(self,curso):
        new_node =  Node(curso)

        if self.is_empty():
            self.Last = new_node
            self.First =  self.Last
        else:
            self.Last.Next = new_node
            new_node.Previuos = self.Last
            self.Last =  new_node
    
    