class Student:
    def __init__(self, name, branch, rno):
        self.sname = name
        self.sbranch = branch
        self.srno = rno

s1 = Student("xyz", "abc", "123")
print(s1)
s2 = Student("pqr", "klm", "456")
print(s2)
str="hi"
print(str)
print(1+2)
print(str.__add__(1,2))