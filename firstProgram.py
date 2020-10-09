
class Answer:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def hcf(self):
        
        if x>y:
            smaller=y
        else:
            smaller=x
        
        for i in range(2, smaller+1):
            if ((x%i==0) and (y%i==0)):
                hat=i
                return hat

if __name__=='__main__':
        x=int(input('what is the smaller number '))
        y=int(input('what is the larger number '))

        byte = Answer(x,y) 
        y=byte.hcf()
        print(y)    




