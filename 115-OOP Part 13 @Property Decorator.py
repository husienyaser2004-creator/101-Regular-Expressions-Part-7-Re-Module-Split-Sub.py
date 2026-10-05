#------------------------------------------------------
#-- Object Oriented Programming => @Property Decorator-
#------------------------------------------------------

from os import name


class Member:

    def __init__(self, name, age):

        self.name = name

        self.age = age 

    def say_hello(self):

        return f"Hello {self.name}" 

    @property
    def age_in_days(self):

        return self.age * 365

one = Member("Hussien", 22)

print(one.name) # Hussien
print(one.age) # 22
print(one.say_hello()) # Hello Hussien
print(one.age_in_days) # 8030

print(one.age_in_days()) # TypeError: 'int' object is not callable
    
      

