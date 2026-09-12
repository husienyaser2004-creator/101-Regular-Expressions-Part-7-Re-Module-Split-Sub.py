#---------------------------
#----Debugging Code---------
#---------------------------

my_list = [1, 2, 3, 4, 5, 6]

my_dictionary = {"Name": "Hussien", "Age": 22, "Country": "Egypt"}

for num in my_list:

    print(num)

for Key, Value in my_dictionary.items():

    print(f"{Key} => {Value}")


def function_one():

    print("Hello From Function One")


function_one()        