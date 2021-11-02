class Node: 
    def __init__(self,curso):
        self.curso = curso
        self.weight = 0 
        self.Next = None
        self.Previuos =  None

class NodeGraph:
    def __init__(self,curso,  list_) -> None:
        self.curso =  curso 
        self.list  =  list_
        self.Next = None
        self.Previuos = None

        