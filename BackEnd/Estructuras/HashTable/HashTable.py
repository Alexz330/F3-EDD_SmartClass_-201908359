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

            tableRehash =  self.rehash(self.table)

            self.table = tableRehash

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
    
    def rehash(self,tableReHash):
        #inicializamos la tabla para el rehash
        arr = []
        for _n in range(self.tableLen):
            newNodo = nodoHash("")
            arr.append(newNodo)
        
        for i in range(self.tableLen):
            if tableReHash[i].carnet != "":
                position  = self.functionHash(tableReHash[i].carnet)
                if arr[position] != None:
                    intento = 0 
                    
                    while True: 
                        
                        if tableReHash[position].carnet == "":
                            arr[position] = tableReHash[i]
                            break
                        
                        # if (position < self.tableLen -1):    
                            # position = self.ColisionCuadratica(int(tableReHash[i].carnet,intento)
                            # intento +=1
                        if position < self.tableLen-1:
                            position = self.ColisionCuadratica(int(tableReHash[i].carnet),intento)
                            intento +=1
                        else:
                            position = 0 
                            intento = 0

                else:   
                    position  = self.functionHash(tableReHash[i].carnet)    
                    arr[position] = tableReHash[i]

        return arr

        
    def get(self,key):
        index =  self.functionHash(key)
    
        return self.table[index].__dict__
    

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

    def getCodigoInterno(self,):         
        etiqueta= "subgraph cluster_0"+"{\n"+"style=filled;\n"+"color=lightgrey;\n"+"node [style=filled,color=white];\n"

        for i in range(self.tableLen):
                if self.table[i].carnet == "":
                    nodo = f"nodoMateria{str(i)} "
                elif self.table[i].carnet != "":
                    nodo = f"nodoMateria{str(self.table[i].carnet)} "
                etiqueta += nodo+"[label =\""+str(self.table[i].carnet)+"\"];\n" 
         
        etiqueta2 = ""
        for n in range(self.tableLen):
            nodo2=""
            contador = 0
            if self.table[n].carnet != "":
                nodo2 = f"nodoMateria{str(self.table[n].carnet)} "
                for m in self.table[n].apunte:
                   
                    nodo_Apunte = f"nodoApunte{str(contador)}{self.table[n].carnet}" 
                    etiqueta2 += f'{nodo_Apunte}[label ="{str(self.table[n].carnet)} {str(contador+1)}-apunte"]\n '

                    etiqueta+= f'{nodo2}-> {nodo_Apunte} '
                   
                    contador+=1
                    nodo2=""
        etiqueta += etiqueta2
        etiqueta+= f'\nlabel ="apuntes"'+"\n}"

        
        return etiqueta 


    def  getCodigoGraphviz(self):
        contenido = self.getCodigoInterno()
        title =  f' labelloc="t";\nlabel="Tabla Hash";'
        return "digraph grafica{\n" +"rankdir=LR;\n" +"node [shape = record, style=filled, fillcolor=seashell2];\n"+title+"\n" +contenido+"}\n";

    def graficar(self,):
        import os 
        f = open('apuntes.dot', 'w', encoding='utf-8')
        f.write(self.getCodigoGraphviz())
        f.close()
        os.system('dot -Tpng apuntes.dot -o apuntes.png')




apuntesitos =  HashTable()

a1 = apunte("tarea 1", "hacer tarea de matematicas")
a2 = apunte("tarea 2", "hacer tarea de estructuras")

apuntesitos.add(201908359,a2)
apuntesitos.add(201908359,a2)
apuntesitos.add(201908359,a2)
apuntesitos.add(201908359,a2)
apuntesitos.add(201909321,a1)
apuntesitos.add(201909321,a2)
apuntesitos.add(201909321,a2)
apuntesitos.add(201909321,a2)
apuntesitos.add(201905435,a2)
apuntesitos.add(201905346,a2)
apuntesitos.add(201906546,a2)
apuntesitos.add(201903453,a1)
apuntesitos.add(201905345,a1)


apuntesitos.graficar()





