import pyttsx3
engine = pyttsx3.init()  

# this is a calculator
num1 = float(input("Enter your first no.: "))
num2 = float(input("Enter your second no.: "))

# assigning variables
mult = '*'
div = '/'
add = '+'
sub = '-'

# asking the operations
operations = input("what will be your operation\nmult\ndiv\nadd\nsub\n = ")

# assigning ifs 

if operations == "mult":
    result = num1 * num2
    engine.say(f"the result of {num1} multiplied by {num2} is {result}")
    print(num1*num2)

elif operations == "div":
    result = num1 / num2
    engine.say(f"the result of {num1} divided by {num2} is {result}")

    print(num1/num2)

elif operations == "add":
    result = num1 + num2
    engine.say(f"the result of {num1} added to {num2} is {result}")

    print(num1+num2)

elif operations == "sub":
    result = num1 - num2
    engine.say(f"the result of {num1} subtracted by {num2} is {result}")

    print(num1-num2)
else:
    
    engine.say(f"sorry the input you have given is wrong please recheck ")

    print("Wrong operation input")

engine.runAndWait()
print("the Program is runned succesfully")