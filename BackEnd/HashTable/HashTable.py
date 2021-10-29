class apunte: 
    def __init__(self,title,content) -> None:
        self.title = title
        self.content =  content

class nodoHash:
    def __init__(self,carnet) -> None:
       self.carnet =  carnet
       self.apunte =  []
    def addApunte(self,apunte):
        self.apunte.append(apunte)
 

class HashTable:
    def __init__(self):
        self.tableLen = 7 
        self.table = [None,None,None,None,None,None,None]
        
        for i  in range(self.tableLen):
            newNode =  nodoHash("")
            self.table[i] = newNode


    def add(self,key,value):
        print()
        position = self.functionHash(key)

        if(self.getPorcentageUse() <= 0.5):
            if self.table[position].carnet == "":
                newNode = nodoHash(key)
                self.table[position] = newNode
                self.table[position].addApunte(value.__dict__)

            elif self.table[position].carnet  ==  key:
                self.table[position].addApunte(value.__dict__)
            else:
                intento = 0
                while True: 
                    
                    if self.table[position].carnet ==  "":
                        
                        newNode = nodoHash(key)
                        self.table[position] = newNode
                        self.table[position].addApunte(value.__dict__)
                        intento = 0 
                        break
                    elif self.table[position].carnet  ==  key:
                        self.table[position].addApunte(value.__dict__)
                        break
                    if position < self.tableLen - 1 :
                       
                             
                        position = self.ColisionCuadratica(key,intento)
                        intento +=1
                    else:
                        position = 0 
                        intento = 0
        else: 
            for i in range (self.getNextNumberPrime(self.tableLen)- self.tableLen):
                newNode = nodoHash("")
                self.table.append(newNode)
            self.tableLen = self.getNextNumberPrime(self.tableLen)

            if self.table[position].carnet ==  "":
                newNode = nodoHash(key)
                self.table[position] = newNode
                self.table[position].addApunte(value.__dict__)

            elif self.table[position].carnet  ==  key:
                    self.table[position].addApunte(value.__dict__)
            
            else:
                intento = 0 
                while True: 
                    
                    if self.table[position].carnet == "":
                        newNode = nodoHash(key)
                        self.table[position] = newNode
                        self.table[position].addApunte(value.__dict__)
                        intento = 0 
                        break
                    elif self.table[position].carnet  ==  key:
                        self.table[position].addApunte(value.__dict__)
                        break
                    if position < self.tableLen -1 :
                        
                        position = self.ColisionCuadratica(key,intento)
                     
                        intento +=1
                    else:
                        position = 0 
                        intento = 0
                       

    def ColisionCuadratica(self, posicion, intento):
        aux =  posicion + intento **2
        return aux % self.tableLen
    
    def rehash(self,table,tableReHash):
        
    def get(self,key):
        pass
    

    def delete(self):
        pass
    def update(self):
        pass

    def getTable(self):
        for i in range(self.tableLen):
            print(f'{str (i)} Carnet: {self.table[i].carnet} - Apuntes: {self.table[i].apunte}')

    def functionHash(self,key):
        return key%self.tableLen
    
    def getPorcentageUse(self):
        counter = 0 
        for i in range(self.tableLen):
            if(self.table[i].carnet != ""):
                counter+=1

        return counter/self.tableLen

    def getNextNumberPrime(self,number):
        while True:
            number+=1
            if(self.isPrime(number)):
                return number
        return 0 

    def isPrime(self, number):
        if(number == 0 or number == 1):
            return False
        for i in range(number - 1,1,-1):
            if ((number%i) == 0):
                return False
        return True



apuntesitos =  HashTable()

a1 = apunte("tarea 1", "hacer tarea de matematicas")
a2 = apunte("tarea 2", "hacer tarea de estructuras")

apuntesitos.add(13,a1)
apuntesitos.add(13,a1)
apuntesitos.add(2,a2)
apuntesitos.add(3,a2)
apuntesitos.add(1,a2)







apuntesitos.getTable()



print(apuntesitos.getPorcentageUse())

