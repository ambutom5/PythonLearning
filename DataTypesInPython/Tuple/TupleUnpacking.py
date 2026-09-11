person = ("Ambu",35,"Btech")                    #Basic Tuple Unpacking
name,age,qualification =  person
print(name)
print(age)
print(qualification)

data = (1,2,3)                                  #Partial Unpacking with _ (ignore values)
first,_,last = data
print(first)
print(last)

x =(1,2,3,4,5)                                  #Extended Unpacking with *
first,*middle,last = x
print(first)
print(middle)
print(last)


y = ((1,2),"Apple")                             #Nested Tuple Unpacking
(first,last),fruit=y
print(first,last)
print(fruit)