#----------------------------------------------
#----------Exceptions Handling-----------------
#-- Try, Except, Else, Finally -----------------
#----------------------------------------------
# Try   => Test The Code For Errors
# Except => Handle The Error
#---------------------------------------------
# Else  => If No Errors
# Finally => Handle The Erros 
#---------------------------------------------

# Number = 10

# Number = int(input("Write Your Age: "))

# print(Number)
# print(type(Number))

try: # Try The Code and Test Errors
    
    Number = int(input("Write Your Age: "))

except : # Handle The Error If Its Found

       print("Bad, this is Not Integer ")

else: # If Theres No Errors
      
    print("Good, This Is Integer")       

finally: # Handle The Error If Its Found

    print("print From Finally Whatever Happens")

try: 

      #print(10 / 0) # ZeroDivisionError
     #print(x)
     print(int("Hello")) # ValueError

except ZeroDivisionError :

     print("Cant Divide") 

except NameError :

     print("Identifier Not Found")

except ValueError :

     print("Value Error Soudy")

except :

     print("Error Happens")     

          
     