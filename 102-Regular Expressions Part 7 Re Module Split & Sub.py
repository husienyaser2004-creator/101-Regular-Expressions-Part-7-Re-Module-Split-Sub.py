#-----------------------------------------------------------
#----Regular Expressions => Re Module Split & Sub ----------
# split(Pattern, String, MaxSplit) => Return A List Of Elements Splitted On Each Match
# sub(pattern, Replace, String, RelaceCount) => Replace Matches With What You Want
#---------------------------------------------------------------------------------------

import re

string_one = " I Love Python Programming Language"

search_one = re.split(r"\s", string_one, 1)

print(search_one)

print("#" * 50)

string_two = "How-To_Write_A_Very-Good-Article"

search_two = re.split(r"-|_", string_two)

print(search_two)

print("#" * 50)

# Get Words From URL

for counter, Word in enumerate(search_two, 1):

    if len(Word) == 1:

        continue

    print(f"Word Number: {counter} => {Word.lower()}")

print("#"* 50)

my_string = "I Love Python"

print(re.sub(r"\s", "-", my_string))




