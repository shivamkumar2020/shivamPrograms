class Student:
    # def __init__(self, name, age):
    def __init__ (self, name, weight, yob):
        self.name= name 
        self.weight= weight
        self.yob= yob
    
    def age (self):
        age1= 2020-int(self.yob)
        
        return age1
        
if __name__=='__main__':
    s1= Student('suresh',38,2001)
    s2= Student('mahesh',45,2003)
    s3= Student('naresh', 10,2004)
    print (s1.name +'\n'+  s2.name + '\n' +s3.name)
    print(s1.age())


    for i in range (0,5):
        x=input('enter the name  ')
        y=input('enter your weight ')
        z=input('enter your yob ')

    s[i]= Student(x,y,z)
# print (s[i].name,s[i].weight,s[i].yob,str(s[i].age()))
# print(str (s4.age()))

print('u')

# import array
# s1='shivam'
# print (s1[2])
# s2=['shivam','krishu']
# from array import*

# res=array('i',[])
# for i in range (2):
#     s2= int(input('enter the next value \n'))
#     res.append(s2)

# print ('my name is' + str(res))




