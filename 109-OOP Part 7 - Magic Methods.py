#------------------------------------------------
#---- object Oriented Programming => ------------
#------------------------------------------------
# Everything in Python is An Object 
# __int__ Called Automatically When Instantianting Class 
# self.__class__ The Class to which a class instance belonges
# __str__ Gives a Human-Readable output of the Object 
# __int__ Returns the Length of the Container 
#------------ Called When We Use the Built-in-len() Function on the object
#----------------------------------------------------------------------



class Skill:


    def __init__(self):

        self.skills = ["Html" , "Css" , "Js"] 

    def __str__(self):

        return f"This is My Skills => {self.skills}"

    def __len__(self):

        return len(self.skills)

profile = Skill()
print(profile)
print(profile.__class__)
print(len(profile))

profile.skills.append("PHP")
profile.skills.append("MySQL")

print(len(profile))

#my_string = "Hussien"
#print(type(my_string))
#print(my_string.__class__)
#print(dir(str))

  
