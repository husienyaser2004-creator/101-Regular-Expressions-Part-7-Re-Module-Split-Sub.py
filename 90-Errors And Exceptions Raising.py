#--------------------------------
#--Errors And Exceptions Raising-
#--------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exceptions Gives You The Message To Understand The Problem
# [3] Exceptions Gives You The Line To Look For The Code In this Line
# [4] Exceptions Have Types (SyntaxError, NameError, TypeError, ValueError, IndexError, KeyError, AttributeError, ZeroDivisionError, FileNotFoundError)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exception
#-----------------------------------------------------

#x = -10

#if x < 0:
#    raise Exception(f" The Number {x} Is Less Than Zero")

#    print("This Will Not print Because The Error")
    
#else:

#    print(f"{x} Is Good Number and Ok" )

#    print("print Message After The condition")


y = "Osama"

if  type(y) != int:

    print("only Numbers Allowed")

    raise ValueError("Only Numbers Allowed")

print('print Message After If condition')    
