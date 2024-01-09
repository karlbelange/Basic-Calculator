#
#-----------------------------
#   Project CST 1101
#-----------------------------
#   24274412
#-----------------------------

def menu():
    print("Choose one of the following options:")
    print("1. Enter an expression (number, operator, number(must be !=0 for division)): ")
    print("2. Quit theprogram.")

#---
def parse(expr):            #returns a list (1st  number, operator, 2nd number)
    expr = expr.strip()     #this method removes spaces before and ater the expression
    if("+" in expr):
        index = expr.find("+")
        operator = "+"
    elif ("-" in expr):
        index = expr.find("-")
        operator = "-"
    elif ("*" in expr):
        index = expr.find("*")
        operator = "*"
    elif ("/" in expr):
        index = expr.find("/")
        operator = "/"
    else:
        return "invalid expression"

    firstNumber = expr[0:index]
    firstNumber = firstNumber.strip()
    secondNumber = expr[index+1:]
    secondNumber = secondNumber.strip()

    print("First number is ",  firstNumber)
    print("Second number is ", secondNumber)

    return [firstNumber, operator, secondNumber]


#---
def calculate(list1):    #list1 = (1st number, operator, 2nd number)
    if (list1[1] == "+"):
        return float(list1[0]) + float(list1[2])
    elif (list1[1] == "-"):
        return float(list1[0]) - float(list1[2])
    elif (list1[1] == "*"):
        return float(list1[0]) * float(list1[2])
    elif (list1[1] == "/"):
        return float(list1[0]) / float(list1[2])
    elif (list[1] == "/" and secondNumber == 0):
        return "reconsider your expression"
    

#---
def main():
    while (True):
        menu()
        print()
        option = str(input("Enter an  option: "))
        if (option == "1"):
            expression = input("Enter an expression: ")
            parse_expression = parse(expression)   #### This function figures out the numbers and operators
            result = calculate(parse_expression)
            print("Result: ", result)
            print()
            print()
        elif (option == "2"):
            break
        
    print("Thank you. See you later.")


#---
main()
        
