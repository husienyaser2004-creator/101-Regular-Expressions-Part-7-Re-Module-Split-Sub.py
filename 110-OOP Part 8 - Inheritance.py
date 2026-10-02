#----------------------------------------------
#-Object Oriented Programming => Inheritance --
#----------------------------------------------

from unicodedata import name


class Food: # Base Class

    def __init__(self, name, Price):

        self.name = name

        self.Price = Price

    def Show(self):

        print(f" {self.name} Is Created From Base Class ")

    def eat(self):

        print("Eat Method From Base Class")

class Apple(Food): # Derived Class

    def __init__(self, name, Price, amount):

        #Food.__init__(self, name, Price) # Create Instance From Base Class 

        super().__init__(name, Price) # Create Instance From Base Class

        self.amount = amount

        print(f" {self.name} Is Created From Derived Class And Price Is {self.Price} And Amount Is {self.amount}")

    def get_from_tree(self):

        print("Get From Tree From Derived Class")    

food_one = Food("pizza", 150) 
food_two = Apple("Pizza",150,500)
food_two.eat()  
food_two.get_from_tree()