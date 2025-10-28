def hello():
    print("hey how are you ?")
hello() # called a function


def greetuser(username, age):
    print("hey " + username + " , how are you ? you are  " + str(age) + " years old.")
greetuser('hooria', 7)
greetuser('hamna', 4)
greetuser('asmara', 17)
greetuser('uvaish',  15)

def sumofAllValues(num):
    return num + num + num 
print(sumofAllValues(10))

def findCube(num):
    return num * num * num
print(findCube(10))

#variables _value - can be used throught the program
#parameter_ arguments- can only be used in a specific functions
