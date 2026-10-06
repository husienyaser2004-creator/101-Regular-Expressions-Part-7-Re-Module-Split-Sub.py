#-------------------------------------------------------------
#--- Object Oriented Programming => ABCs Abstract Base Class -
#-------------------------------------------------------------
# Class Called Abstract Base Class If It Has One Or More Abstract Methods
# abc Moudule in Python provides Infrastructure For Defining Custom Abstract Base Classes 
# By Adding @abstractmethod Decorator on the Method
# ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class 
#------------------------------------------------------------------------------------------
 
from abc import ABCMeta, abstractmethod

class Programming(metaclass=ABCMeta):

    @abstractmethod
    def has_oop(self):

        pass

    def has_name(self):

        pass

class Python(Programming):

    def has_oop(self):

        return "Yes"    

class Pascal(Programming):  
    
    def has_oop(self):

        return "No"

    def has_name(self):

        return "Pasecal"

one = Python()
print(one.has_oop()) # Yes          