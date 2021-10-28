class apunte:
    titulo:str
    contenido:str

class nodoHash:
    carnet:int
    apuntes:list = [apunte]



class HashTable:
    def __init__(self):
        self.tableLen = 7 
        self.table = [None,None,None,None,None,None,None]
        


    def add(self,key,value):
        position = self.functionHash(key,self.tableLen)
        if(self.getPorcentageUse(self.tableLen) <= 0.5):
            if self.table[position] == None:
                

    def get(self,key):
        pass

    def delete(self):
        pass
    def update(self):
        pass
    def functionHash(self,key,length):
        return key%length
    def getPorcentageUse(self,length):
        counter = 0 
        for i in self.table:
            if(i is not None):
                counter+=1

        return counter/length

apuntes =  HashTable()

print()




