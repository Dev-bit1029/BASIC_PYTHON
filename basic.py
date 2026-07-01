print("STRING METHOD ")
print(" ")


Name = "HELLO SIR  👋"
print(Name.lower())

a = "hey sir"
print(a.upper())

b = "jamnagar                         "
print(b.strip())

c = "hello dev thakkar"
print(c.replace("dev thakkar","bhavya"))

d = "hello sir"
print(d.split())

f = "indrajit"
f = "-".join(f)
print(f)

g = "harshil"
print(g.find("h"))

print("LIST METHOD ")
print(" ")

num1 = [1,2,3,4,5,6,7,8,9]
num1.append(10)
print(num1)

num2 = [1,2,3,4,5,6,7,8,9]
num2.insert(0,0)
print(num2)

num3 = [1,2,3,4,5,6,7,8,9]
num3.remove(5)
print(num3)

num4 = [1,2,3,4,5,6,7,8,9]
num4.pop()
print(num4)

num5 = [19,8,7,4,5,6,3,2,1]
num5.sort()
print(num5)

num6 =[1,2,3,4,56,6,7,8,9]
num6.reverse()
print(num6)

num7 = [1,2,3,4,5,6,5,6,7,8,9,78]
num7.extend([1,2])
print(num7)


print("DICTINARY  METHOD ")
print(" ")

A = {
    "NAME":"DEV",
    "AGE":20
}
print(A.keys())
print(A.values())
print(A.items())
print(A.get("NAME"))


print(A)

A = {
    "NAME":"DEV",
    "AGE":20,
    "MARK":65
}

B = A.update({"AGE":50})
print(A)

C = A.pop("AGE")
print(A)

