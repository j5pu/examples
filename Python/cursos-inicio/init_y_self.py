#!/usr/bin/python
class Person:
    """Cuando hay __init__(self) todas las funciones tienen que tener show(self) - Person"""

    def __init__(self, name, batch_size=100):
        """Doc - __init__ Constructor - Person"""
        global self_
        self_ = self
        self.batch_size = batch_size
        self.n_name = name
        """Aqui ha destruido __del__ uno de los que habia cuando se llama con p=Person()"""
        print ('__init__ -', self.n_name)

        global self_n_nombre
        self_n_nombre = self.n_name

    def show(self, n1, n2):
        """Doc - Inside Show - Person"""
        print (self.n_name)
        print ("Sum = ", n1 + n2)

    def __del__(self):
        print ("Destructor Deleting object - Person - ", self.n_name)

class Person1:
    """Cuando hay __init__(variable) todas las funciones tienen que tener show(self) y self = variable - Person1"""

    def __init__(mi_nombre, batch_size):
        """Doc - __init__ Constructor - Person1 """
        global self_
        self_ = mi_nombre
        mi_nombre.batch_size = batch_size
        mi_nombre.n_name = batch_size
        global self_n_nombre
        self_n_nombre = mi_nombre.n_name
        print (mi_nombre.n_name)


    def show1(self, n1, n2):
        """Doc - Inside Show - Person1"""
        print (self.n_name)
        print ("Sum = ", n1 + n2)

    def __del__(self):
        print ("Destructor Deleting object - Person1 - ", self.n_name)


class Person2:
    """Cuando no hay __init__() las variables de las funciones show(n1, n2) no van a self y las variables son locales a ese trozo, pero se leen antes del main o de llamar a Person2 - Person1"""
    global n_name
    n_name = 'CACA'

    def show2(n1, n2):
        """Doc - Inside Show - Person2"""
        print (n_name)
        print ("Sum = ", n1 + n2)

    def __del__():
        print ("Destructor Deleting object - Person2 - ")

print (n_name)

print(__doc__)
print (Person.__doc__)
print (Person.__init__.__doc__)
print (Person.show.__doc__)

print ("- Comienza: Jay")
p=Person('Jay')
p.show(2, 3)
print("self_n_nombre:", self_n_nombre)

print (p.__doc__)
print (p.__init__.__doc__)
print (p.show.__doc__)
print ("- Acaba: Jay")

print ("- Comienza: Jose")
"""No Destruye __del__ ninguno """
Person('Jose')
"""Con esta no es que coja el Jose del __init__ ya que el Person('Jose') no ha llamado al __init__ sino que se lo paso sen self_ """

Person.show(self_, 4, 5)
print("self_n_nombre:", self_n_nombre)

print (p.__doc__)
print (p.__init__.__doc__)
print (p.show.__doc__)
print ("- Acaba: Jose")

print ("- Comienza: Victor")
"""No Destruye __del__ ninguno """
Person('Victor')
"""Con esta daría errir el Jose del __init__ ya que el Person('Jose') no ha llamado al __init__ sino que se lo paso sen self, al no estar definidio self entonces espera 3 parametros y le paso 2 """

"""Person.show(4, 5)
Daria error porque no tiene el self definido en la llaada de Person('Victor')"""
print("self_n_nombre:", self_n_nombre)

print (p.__doc__)
print (p.__init__.__doc__)
print (p.show.__doc__)
print ("- Acaba: Jose")

print ("- Comienza: Perico")
"""Destruye __del__ el que se llama directamente al ser misma llamada Person('Jose') pero no el  p=Person('Jay')"""
Person('Perico')
Person.show(self_, 4, 5)
print("self_n_nombre:", self_n_nombre)

print (p.__doc__)
print (p.__init__.__doc__)
print (p.show.__doc__)
print ("- Acaba: Perico")

print ("- Comienza: Manolo")
"""Destruye __del__ el que se llama funcion Person('Perico') pero no el p=Person('Jay')"""
p=Person('Manolo')

"""Aqui ha destruido el otro __del__  p=Person('Jay'"""
print('__main__ -', self_n_nombre)
p.show(6, 7)
print("self_n_nombre:", self_n_nombre)

print (p.__doc__)
print (p.__init__.__doc__)
print (p.show.__doc__)
print ("- Acaba: Manolo")

print ("- Comienza: Antonio")
p=Person1('Antonio')
p.show1(8, 9)
print("self_n_nombre:", self_n_nombre)

print (p.__doc__)
print (p.__init__.__doc__)
print (p.show1.__doc__)
print ("- Acaba: Antonio")

print ("- Comienza: Juan")
Person1('Juan')
Person1.show1(self_, 10, 11)
print("self_n_nombre:", self_n_nombre)

print (p.__doc__)
print (p.__init__.__doc__)
print (p.show1.__doc__)
print ("- Acaba: Juan")

print ("- Comienza: Luis")
p=Person1('Luis')
p.show1(12, 13)
print("self_n_nombre:", self_n_nombre)

print (p.__doc__)
print (p.__init__.__doc__)
print (p.show1.__doc__)
print ("- Acaba: Luis")

print ("- Comienza: Pedro")
Person2.show2(14, 15)
print("self_n_nombre:", self_n_nombre)

print (Person2.__doc__)
print (Person2.show2.__doc__)
print ("- Acaba: Pedro")

class Person3:

    '''Doc - Inside Class '''

    def __init__(self, name):
        '''Doc - __init__ Constructor'''
        self.n_name = name

    def show3(self, n1, n2):
        '''Doc - Inside Show'''
        print (self.n_name)
        print ('Sum = ', n1 + n2)

    def __del__(self):
        print ('Destructor Deleting object - ', self.n_name)

p=Person3('Ana')
p.show3(2, 3)
print (p.__doc__)
print (p.__init__.__doc__)
print (p.show3.__doc__)

p=Person3('Maria')
p.show3(2, 3)
print (p.__doc__)
print (p.__init__.__doc__)
print (p.show3.__doc__)

p=Person3('Carmen')
p.show3(2, 3)
print (p.__doc__)
print (p.__init__.__doc__)
print (p.show3.__doc__)

p=Person3('Juana')
p.show3(2, 3)
print (p.__doc__)
print (p.__init__.__doc__)
print (p.show3.__doc__)


class MyClass(object):
    i = 123

    def __init__(self):
        print('Solo asignando a = MyClass() entra en __init__')
        self.i = 345


a = MyClass()
print ('Variable dentro del objeto: a.i = ', a.i)
print ('Variable dentro de la clase: MyClass.i = ', MyClass.i)
