#------------------------------------------------------------------------------------
#--Object Oriented Programming => Multiple Inheritance And Method Overriding---------
#------------------------------------------------------------------------------------

from unittest.mock import Base


class Baseone:

    def __init__(self):

        print("Base One")

    def func_one(self):

        print("one")   

class Basetwo:

    def __init__(self):

        print("Base Two")

    def func_two(self):

        print("Two")   

class Derived(Baseone, Basetwo):


    pass

my_var = Derived() # Base One

#print(Derived.mro()) # Method Resolution Order

print(my_var.func_one)
print(my_var.func_two)

my_var.func_one()
my_var.func_two()


class Base:

    pass

class Derivedone(Base):

    pass

class DerivedTwo(Derivedone):

    pass
