#---------------------------------------------------------------------
#----OOP (object Oriented Programming) Class Syntax And Info----------
#---------------------------------------------------------------------
# [1] Class is The Blueprint Or Construtor Of The Object
# [2] Class Instantiate Means Create Instance Of A Class 
# [3] Instance => Object Created From Class And HAve Their Methods And Attributes
# [4] Class Defined With KeyWord Class 
# [5] Class Name Writtem With Pascalcase [UpperCamel Case] Style
# [6] Class May Contains Methods and Attributes
# [7] When Creating Object Python Look For The Built In __init__ Method
# [8] __init__ Method Called Every Time You Create Object From Class 
# [9] __init__ Method Is Initialize The Data For The Object 
# [10] Any Method With Two Underscore in The Start and End Called Dunder Or Magic Method
# [11] Self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] Self Can Be Named Anything 
# [13] In PYthon You Dont Need TO CAll new() KeyWord To Create Object
#----------------------------------------------------------------------------------------------

# Syntax 
# Class Name: 
#      Constuctor => Do Instation [ Create Instance From A Class ]
#      Each Instance IS Separate Object 
#      def __init__ (self, other_data)
#        Body Of Function

class Member:

     def __init__(self):

        print("A New Member Has Been Added")


#Member()
#Member()
#Member()

member_one = Member()
member_two = Member()
member_three = Member()


my_dictionary = {
    'name' : "Hussien",
    'age' : 22,
    'monthly_salary':5000,
    'yearly_salary' : '' #Something
}
