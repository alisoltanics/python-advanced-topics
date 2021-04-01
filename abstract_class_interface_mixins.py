1. Abstract Class
Class that needs to contain one or more abstract methods
Abstract Class can contain state (instance variables) and non-abstract methods


2. Interface
Interface contains abstract methods only (no non-abstract methods and no internal state)


3. MixIns
MixIns (like Interfaces) do not contain internal state (instance variables)
MixIns contain one or more non-abstract methods (they can contain non-abstract methods unlike interfaces)


In e.g. Python these are just conventions, because all of the above are defined as classes. However, the common feature of both Abstract Classes, Interfaces and MixIns is
that they should not exist on their own, i.e. should not be instantiated.



##############################################################################################3

ABSTRACT CLASS:



# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")

class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")

class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 4 sides")

# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

##############################################################################################


##############################################################################################
MIXIN CLASS:


class MyMixin:

    def setname(this, name):
        this.name = name

    def getname(this):
        return this.name

class MyClass(MyMixin):
    def __init__(self):
        self.name = "Default"

my_object = MyClass()
username = my_object.getname()
##############################################################################################











# https://www.kite.com/python/answers/how-to-use-mixins-in-python
# https://stackoverflow.com/a/59752820/6173668