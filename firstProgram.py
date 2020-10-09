class Tank:
    def __init__(self,week):
        self.week=week

    def switch(self, Week):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(Week), lambda: default)()

    def case_1(self):
        return "Monday"
 
    def case_2(self):
        return "Tuesday"
 
    def case_3(self):
        return "Wednesday"


if __name__=='__main__':
    n= int(input('enter the number? '))
    byte = Tank(n) 
    y=byte.switch(n)
    print(y)      