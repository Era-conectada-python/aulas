class Singleton:
   __instance = None

   @staticmethod 
   def getInstance():
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance

   def __init__(self):
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self

s = Singleton()
print(s)

s2 = Singleton.getInstance()
print(s2)

##############################################################

class MakeMeal:

   def prepare(self): pass
   def cook(self): pass
   def eat(self): pass

   def go(self):
      self.prepare()
      self.cook()
      self.eat()

class MakePizza(MakeMeal):
   def prepare(self):
      print("Prepare Pizza")
   
   def cook(self):
      print("Cook Pizza")
   
   def eat(self):
      print("Eat Pizza")

class MakeTea(MakeMeal):
   def prepare(self):
      print("Prepare Tea")
   
   def cook(self):
      print("Cook Tea")
   
   def eat(self):
      print("Eat Tea")

makePizza = MakePizza()
makePizza.go()

print(25*"+")

makeTea = MakeTea()
makeTea.go()
