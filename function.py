import ast 

l = ["sahadji","krishna","mohan","raj"]

file = open("funtry.py","w")
file.write(str(l))
file.close()

file = open("funtry.py", "r")
a = ast.literal_eval(file.read())
file.close()

file = open("funtry.py","w")
a.append("manmohan")
file.write(str(a))
file.close()

file = open("funtry.py", "r")
a = ast.literal_eval(file.read())
file.close()

file = open("funtry.py","w")
a.pop()
file.write(str(a))
file.close()

file = open("funtry.py", "r")
a = ast.literal_eval(file.read())
file.close()

file = open("funtry.py","w")
a.insert(1,"jaishree") 
file.write(str(a))
file.close()

file = open("funtry.py", "r")
a = ast.literal_eval(file.read())
file.close()

file = open("funtry.py","w")
a.remove("mohan")
file.write(str(a))
file.close()


file = open("funtry.py", "r")
a = ast.literal_eval(file.read())
file.close()

file = open("funtry.py","w")
a.reverse()
file.write(str(a))
file.close()

file = open("funtry.py", "r")
a = ast.literal_eval(file.read())
file.close()

file = open("funtry.py","w")
a.sort()
file.write(str(a))
file.close()

import math

a = 100
b = 10
c = -102

print(math.sqrt(a))
print(math.pow(a,2))
print(math.factorial(b))
print(math.fabs(c))
print(math.gcd(a,b))
print(math.pi)

