#---------------------------------------------------
#---Object Oriented Programming => Polymorphism ----
#---------------------------------------------------

n1 = 10
n2 = 20

print(n1 + n2) # 30

s1 = "Hello"
s2 = "HUssien"
print(s1 + " " + s2) # Hello World

print(len([1, 2, 3, 4, 5, 6])) # 6
print(len("Hello Hussen"))
print(len({"Key_One": 1 , "Key_Two": 2}))  # 2

class A: 
    
    def do_something(self):

        print("From Class A")

        raise NotImplementedError("Derived class Must Implement this method")

class B(A):

    def do_something(self):

        print("From Class B")

class C(A):

    def do_something(self):
        
        print("From Class C")
        

my_instance = C()
my_instance.do_something() # From Class C
