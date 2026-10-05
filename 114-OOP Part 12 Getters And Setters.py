#-----------------------------------------------------
#--Object Oriented Programming => Getters And Setters-
#-----------------------------------------------------

class Member:
    def __init__(self, name):

        self.__name = name # Private

    def say_hello(self):

        return f"Hello {self.__name}"

    def get_name(self): # Getter
        return self.__name

    def set_name(self, new_name): # Setter

        self.__name = new_name

one = Member("Hussien")

print(one.get_name()) # Hussien
one.set_name("soudy")
print(one.get_name()) # soudy