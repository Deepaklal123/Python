#Author:    Deepak Lal
#University:Sukkur IBA University

a=3
b=4
#Arthmetic operators
print("The sum of 3+4 is ", 3+4)
print("The sum of 3-4 is ", 3-4)
print("The sum of 3*4 is ", 3*4)
print("The sum of 3/4 is ", 3/4)

# Assignment operators
a=32
a+=2     #a=a+2
print(a) # a=34

#Comparison Operators
b=(12>23)
print(b)    #prints False
b=(12<23)   #prints True
print(b)
b=(23>=12)
print(b)
b=(12==23)
print(b)
b=(12!=23)
print(b)


# logical operators
bool1=True
bool2=False
print("The value of bool1 and bool2", (bool1 and bool2))
print("The value of bool1 or bool2", (bool1 or bool2))
print("The value of not bool2",(not bool2))