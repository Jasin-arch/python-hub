"""
-input value 1
-select operator
-input value
-calculate
-print out the alue/solution
"""

print("========================")
valueOne = input("Enter the firt operand: ")
valueTwo = input("Ente the second value: ")

operatorChoice = input("""
 Kindly input the number of the operation you want: \n
  1. additio(+)
  2. substration(-)
  3. multiplication(*)
  4. division(/)
  5. power(**)
  6. floor division(division without decimal)

""")


output = ""
operatorChoice = int(operatorChoice)
valueOne = int(valueOne)
valueTwo = int(valueTwo)

if(operatorChoice == 1):
    output = valueOne + valueTwo
elif(operatorChoice == 2):
    output = valueOne - valueTwo
elif(operatorChoice == 3):
    output = valueOne * valueTwo
elif(operatorChoice == 4):
    output = valueOne / valueTwo
elif(operatorChoice == 5):
    output = valueOne ** valueTwo
elif(operatorChoice == 6):
    output = valueOne // valueTwo
else:
    output ="wrong selection"

output =""
match(operatorChoice):
    case 1:
        output = valueOne + valueTwo
    case 2:
        output = valueOne - valueTwo
    case 3:
        output = valueOne * valueTwo
    case 4:
        output = valueOne / valueTwo
    case 5:
        output= valueOne ** valueTwo
    case 6:
        output = valueOne // valueTwo
    case _:
     output = "invalid!"

print("***********************")
print(output)
print("***********************")


def greeting():
    print("greeting")
    

    



