#Program to generate Product Code.

import random

def codeGenerator():
    n = int(input("No. of PC to generate: "))
    random_list = []
    for i in range(0, n):
        random_list.append(random.randint(100, 1000000))
    for n in random_list:
        print(n)
        
codeGenerator()