#----------------------------------------------------------
#----OOP => Instance Attributes And Methods Part 1---------
#----------------------------------------------------------
# Self : Point To Instance Created From Class
# Instance Attributes : Instance Attributes Defined Inside The Constructor
#--------------------------------------------------------------------------
# Instance Methods : Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Lik Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
#----------------------------------------------------------------------------

class Member :

    def __init__(self):

        self.name = "Hussien"

member_one = Member() 
member_two = Member()
member_three = Member()

# print(dir(member_one))

print(member_one.name)
print(member_two.name)
print(member_three.name)



class Member :

    def __init__(self, first_name, middle_name, last_name):

        self.fname = first_name

        self.mname = middle_name

        self.lname = last_name



member_one = Member("Hussien" , "Yasser" , "Soudy") 
member_two = Member("Ali" , "Hussien" , "Yasser")
member_three = Member("Noah" , "Hussien" , "Yasser")

# print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname,member_two.mname, member_two.lname)
print(member_three.fname,member_three.mname, member_three.lname)


