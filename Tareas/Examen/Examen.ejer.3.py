class Queue:
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.insert(0,item)

  def dequeue(self):
    return self.items.pop()

  def adelantar_elemento_N(self,n): #Metodo que se agrega
    error = None
    prov = []
    if n>len(self.items):
      error = True
    else:
      error = False
      for i in range(1,n):
        prov.append(self.dequeue())
    prov.insert(0,self.dequeue())
    prov.reverse()
    if len(self.items)!=0:
      for i in range(1,len(self.items)+1):
        prov.insert(0,self.dequeue())
    prov.reverse()
    for i in prov:
      self.enqueue(i)
    if error==False:
      print True
      print self.items
    else:
      print False
      print "No hay elemento en la posicison",n

def encolar(cola,lista_elementos):
  for i in lista_elementos:
    cola.enqueue(i)

def main3():
  print "En la lista:", elementos
  n = int(raw_input("De la posicison del elemento que desea adelantar"))
  cola.adelantar_elemento_N(n)

#Programa

cola = Queue()
elementos = [i for i in range(10)]
encolar(cola,elementos)
