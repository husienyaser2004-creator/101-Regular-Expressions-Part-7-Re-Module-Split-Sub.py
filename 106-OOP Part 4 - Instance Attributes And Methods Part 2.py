#---------------------------------------------------
#---OOP => Instance Attributes And Methods Part 2---
#---------------------------------------------------
class Member :

    def __init__(self):

        self.name = "Hussien"

member_one = Member() 
member_two = Member()
member_three = Member()

# print(dir(member_one))

#print(member_one.name)
#print(member_two.name)
#print(member_three.name)



class Member :

    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name

        self.mname = middle_name

        self.lname = last_name

        self.gender = gender

    def full_name(self):

        return f"{self.fname} {self.mname} {self.lname}"

    def name_with_title(self):

        if self.gender == "Male" :

            return f"Hello Mr {self.fname}"

        elif self.gender == "Female" :

            return f"Hello Miss {self.fname}"

        else:

            return f"Hello{self.fname}"

    def get_all_info(self):

        return f"{self.name_with_title()}, Your Full Name Is: {self.full_name}"

member_one = Member("Hussien" , "Yasser" , "Soudy", "Male") 
member_two = Member("Ali" , "Hussien" , "Yasser", "Male")
member_three = Member("Noah" , "Hussien" , "Yasser" , "Female")

# print(dir(member_one))

#print(member_one.fname, member_one.mname, member_one.lname)
#print(member_two.fname,member_two.mname, member_two.lname)
#print(member_three.fname,member_three.mname, member_three.lname)

#print(member_one.full_name())
#print(member_one.name_with_title())

print(member_one.get_all_info())
