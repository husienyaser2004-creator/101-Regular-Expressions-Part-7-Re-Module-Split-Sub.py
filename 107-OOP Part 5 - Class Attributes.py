#------------------------------------------------
#------- OOP => Class Attributes ----------------
#------------------------------------------------


class Member :

    not_allowed_names = ["Hell","Shit", "Baloot" ]

def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name

        self.mname = middle_name

        self.lname = last_name

        self.gender = gender

def full_name(self):

    if self.fname in Member.not_allowed_names:

        raise ValueError("Name Not Allowed")

    else:

        return f"{self.fname} {self.mname} {self.lname}"

def name_with_title(self):

        if self.gender == "Male":

            return f"Hello Mr {self.fname}"

        elif self.gender == "Female":

            return f"Hello Miss {self.fname}"

        else:

            return f"Hello{self.fname}"

def get_all_info(self):

        return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"



member_one = Member("Hussien" , "Yasser" , "Soudy", "Male") 
member_two = Member("Ali" , "Hussien" , "Yasser", "Male")
member_three = Member("Noah" , "Hussien" , "Yasser", "Famela")
member_four = Member("Shit","Hell","Metal" , "Famale")

# print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname,member_two.mname, member_two.lname)
print(member_three.fname,member_three.mname, member_three.lname)

# print(member_two.full_name())
# print(member_two.name_with_title())

#print(member_four .get_all_info())

# print(dir(Member))



