class Student:
    fee_hike =1.02
    def __init__(self, name, branch, rno,fee,yoj):
        self.sname = name
        self.sbranch = branch
        self.srno = rno
        self.sfee=fee
        self.syoj=yoj
    @classmethod
    def hike(cls):
       return "i am a class method"
                
                    
    
    def name(self):      # instance methods
        print(self.name)
    def __repr__(self):
       return f"{self.sname},{self.sbranch},{self.srno},{self.sfee},{self.syoj}"
    def __str__(self):
        return f"{self.sname},{self.sbranch},{self.srno},{self.sfee},{self.syoj}"
s1 = Student("xyz", "abc",123,20000,2024)
print(s1)
