class Person:
    def __init__(self,name,age):
        self._name = name
        self.age = age
    
    def getName(self):
        return self._name

dude1 = Person("John",33)

#Call method, it works
print(dude1.getName())

#Access private attribute
print(dude1._name)

#Access public attribute
print(dude1.age)

#Modify public attibute from outside the Class
dude1.age = 55
print(dude1.age)

#Now we access the private attribute incorrectly, triggering an error
print(dude1.name)
