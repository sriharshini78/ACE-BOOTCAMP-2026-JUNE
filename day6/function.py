class Student:
    def __init__(self, name, branch, rno):
        self.sname = name
        self.sbranch = branch
        self.srno = rno

s1 = Student("xyz", "abc", "123")
s2 = Student("pqr", "klm", "456")

print(s1.sname)
print(s1)