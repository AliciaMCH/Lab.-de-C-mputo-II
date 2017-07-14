#Clases
class Stack:
  def __init__(self):
     self.items = []

  def isEmpty(self):
     return self.items == []

  def push(self, item):
     self.items.append(item)

  def pop(self):
     return self.items.pop()

  def peek(self):
     return self.items[len(self.items)-1]

  def size(self):
     return len(self.items)

class Llamadas:
  def __init__(self):
    self.Llamadas_realizadas = []
    self.Llamadas_facturadas = []

#Funciones

def hacer_llamada(extensiones,numTels,Llamadas):
  status = 0
  ext = random.choice(extensiones)
  numTel = random.choice(numTels)
  fecha = [random.randint(2013,2017),random.randint(1,212),random.randint(1,28)]
  hora = [random.randint(0,23),random.randint(1,59)]
  duracion = random.randrange(6)
  valor = False
  datos_llamada = [fecha,hora,numTel,ext,duracion,valor]
  if Llamadas.Llamadas_realizadas == []: #Agregar primer elemento
    pila_numTel = Stack()
    pila_numTel.push(datos_llamada)
    Llamadas.Llamadas_realizadas.append([numTel,pila_numTel])
    status = 1
  else:
    for i in Llamadas.Llamadas_realizadas:
      if i[0]==numTel:
        i[1].push(datos_llamada)
        status = 2
      else:
        pila_numTel = Stack()
        pila_numTel.push(datos_llamada)
        Llamadas.Llamadas_realizadas.append([numTel,pila_numTel])
        status = 3
  print status
def main2():
  print "De los siguientes numeros:", numTels
  r = raw_input("Indique la posicion del numero que desea facturar (El primer numero tiene posicion 1)")
  if r <= len(numTels):
    desde = raw_input("Fecha de Inicio aaaa/mm/dd").split("/")
    desde_int =  [int(i) for i in desde]
    hasta = raw_input("Fecha de Fin aaaa/mm/dd").split("/")
    hasta_int = [int(i) for i in hasta]
    Llamadas.facturar_llamadas_por_fecha(numTels[r-1],desde_int,hasta_int)
  else:
    print "La posicion indicada no existe en la lista"
    main2()

#Programa

import random
extensiones = [1122,1123,1124,1125]
numTels = [i for i in range(3265447,3265450)]

Llamadas = Llamadas()
for i in range(4):
    hacer_llamada(extensiones,numTels,Llamadas)
print Llamadas.Llamadas_realizadas
