#-----------------------------------------------------
#----Advanced Lessons - Timing Your Code With Timeit--
#-----------------------------------------------------
#--- timeit: Get Execution  Time Of Code By Running 1M Time And Give You Minimal Time 
#            It Used For Performace By Testing All Functionally 
#   timeit(stmt, setup, timer, number)
#   timeit(pass, pass, defauIt, 1.000.000) Defauit Values
#---------------------------------------------------------------
#- stmt: Code You Want To Measure The Excution Time
#  Setup: Setup Done Before The Code Execution (Import Module Anything)
#  timer: The Timer Value 
#  number: How Many Execution That Will Run
#----------------------------------------------------------------

import timeit
#import random

# print(dir(timeit))

# print(timeit.timeit("'Soudy' * 1000"))

# name = "Soudy"
# print(name*1000)

# print(timeit.timeit("name = 'Soudy'; name * 1000"))

# print(random.randint(0, 50))

print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))



