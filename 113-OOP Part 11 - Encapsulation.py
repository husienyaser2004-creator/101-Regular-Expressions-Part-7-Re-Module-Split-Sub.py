#---------------------------------------------------------
#---- Object Oriented Programming=> Encapsulation --------
#---------------------------------------------------------
# Encapsulation 
#-- Restrict Access To The Data Stored In Attirbutes and Methods
#Public => Can Be Accessed From Anywhere
#-- Every Attribute and Method That We Used So Far Is Public
#- Attribute and Method can Be Modfied And Run From Everywhere
#-- Inside our outside The Class 
# Protected =>
#--Attribute and Method Can Be Accessed From Within The Class And Sub Classes
#--Attribute and Method prefixed With Underscore _
#Pravate =>
#-- Attribute and Method Can Be Accessed From Within The Class or Object Only
#--Attribute Cannont Be Modified From Outside the Class
#--Attribute and Method prefixed With Double Underscore __
#-----------------------------------------------------------------------
#-- Attribute = Variables = Properties
#-----------------------------------------------------------------------

class Member:
    def __init__(self, name):

        self.name = name # Public Attribute

one = Member("Hussien")

print(one.name) # Hussien

one.name = "soudy"

print(one.name) # soudy

print("#" * 50)

class Member:
    def __init__(self, name):

        self._name = name # Protected

one = Member("Hussien")

print(one._name) # Hussien

one._name = "soudy"

print(one._name) # soudy


print("#" * 50)


class Member:
    def __init__(self, name):

        self.__name = name # Private

    def say_hello(self):

        return f"Hello {self.__name}"

one = Member("Hussien")

print(one.say_hello()) # Hello Hussien

one.__name = "soudy"

print(one.say_hello()) # Hello Hussien

print(one._Member__name) # soudy
