from math import sin
from math import cos
from math import tan
from math import exp

def Calculator():

    calc = input("What kind of calculation do you wish to do? (type ? for help): ")

    if calc == "?":
        print("Currently supported: multiplication(*), division(/), addition(+), square (sq), subtraction (-) and modulo (%)")
        print("")
        Calculator();

    elif calc == "*":
        print("")
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))
        print("Answer: ", number1 * number2)
        print("")
        Calculator();

    elif calc == "sq":
        print("")
        number1 = int(input("Please select the first number: "))
        print("Answer: ", number1 * number1)
        print("")
        Calculator();

    elif calc == "/":
        print("")
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 / number2)
        print("")
        Calculator();

    elif calc == "-":
        print("")
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 - number2)
        print("")
        Calculator();

    elif calc == "+":
        print("")
        number1 = int(input("Please select the first number: "))
        number2 = int(input("Please select the second number: "))

        print("Answer: ", number1 + number2)
        print("")
        Calculator();

    elif calc == "%":
        print("")
        try:
            number1 = int(input("Please select the first number(greater): "))
            number2 = int(input("Please select the second number(smaller): "))
        except (TypeError, ValueError):
            print("Invalid input")
            print("")
            Calculator();
        if(abs(number1)<abs(number2)):
           print("")
           print("The second number entered is greater than the bigger number")
           print("")
           Calculator();
        print("Answer: ", number1-number2*int(number1/number2))
        print("")
        Calculator();
        
    elif calc == "%%":
        print("x")
        number1 = float(input("Please select the first number: "))
        number2 = float(input("Please select the second number: "))
        try:
            value = (number1 / number2) * 100
            print("Answer: ", value)
            print("")
            Calculator();        
        except(TypeError, ValueError, ZeroDivisionError):
            print("Invalid input")
            print("")
            Calculator()            
        
    elif calc == "exp":
        print("")
        number1 = float(input("Please select the first number: "))
        try:
            value = exp(number1)
            print("Answer: ", value)
            print("")
            Calculator() 
        except(TypeError, ValueError, ZeroDivisionError):
            print("Invalid input")
            print("")
            Calculator()            
        
    elif calc == "sin":
        print("")
        number1 = float(input("Please select the first number (rad): "))
        print("Answer: ", sin(number1))
        print("")
        Calculator()

    elif calc == "cos":
        print("")
        number1 = float(input("Please select the first number (rad): "))
        print("Answer: ", cos(number1))
        print("")
        Calculator()               
        
    elif calc == "tan":
        print("")       
        number1 = float(input("Please select the first number (rad): "))
        try:
            value = tan(number1)
            print("Answer: ", value)
            print("")
            Calculator()
        except (TypeError, ValueError. ZeroDivisionError):
            print("Invalid input")
            print("")
            Calculator()        
                
    elif calc == "exit":
        exit();

    else:
        print("")
        print("Terribly Sorry, I don't understand your request. Currently supported calculations: *, /, -, + and % (MODULO). Sorry for the inconvenience!")
        print("")
        Calculator();

print("")
Calculator();
