#Author: EAF 11/10/22
valueOne = int(input("Enter a numeric value: "))
valueTwo = int(input("Enter a numeric value: "))
valueThree = int(input("Enter a numeric value: "))
#creates variable that converts to integer and stores the user inputted value
list = [valueOne, valueTwo, valueThree]
print(list)
if valueOne%2 == 0 and valueTwo%2 ==0 and valueThree %2 == 0:
    print("even")
elif valueOne%2 != 0 and valueTwo%2 != 0 and valueThree %2 != 0:
    print("odd")
else:
    print("mixed")