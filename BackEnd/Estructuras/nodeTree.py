class node:

    def __init__(self,student):
        
        self.student = student
        self.right =  None
        self.left =  None 
        self.height  = 0
    
    def getCodigoInterno(self):
        etiqueta= ""
        if self.left is None and self.right:
            etiqueta = "nodo"+str(self.student.no_carnet)+"[label =\""+self.student.name+"\"];\n"
        else:
            etiqueta="nodo"+str(self.student.no_carnet)+" [ label =\"<C0>|"+str(self.student.no_carnet)+"\\n"+self.student.name+"\\n "+self.student.career+"|<C1>\"];\n";

        if self.left != None:
            contenido = self.left.getCodigoInterno()
            etiqueta=etiqueta + str(contenido) +"nodo"+str(self.student.no_carnet)+":C0->nodo"+str(self.left.student.no_carnet)+"\n"; 
        
        if(self.right!=None):
            contenido = self.right.getCodigoInterno() 
            etiqueta=etiqueta + str(contenido) +"nodo"+str(self.student.no_carnet)+":C1->nodo"+str(self.right.student.no_carnet)+"\n";                    
        
        return etiqueta;

    def  getCodigoGraphviz(self):
            contenido = self.getCodigoInterno()
            return "digraph grafica{\n" +"rankdir=TB;\n" +"node [shape = record, style=filled, fillcolor=seashell2];\n"+contenido+"}\n";
          
    
