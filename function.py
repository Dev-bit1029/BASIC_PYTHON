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