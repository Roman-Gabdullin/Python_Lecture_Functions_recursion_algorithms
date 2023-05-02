# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def step(a, b):
    if b == 1: return a
    elif b == 0 or a == 1: return 1
    elif a == 0:return 0
    return step(a,b-1)*a 


A = int(input())
B = int(input())

print(step(A,B))



