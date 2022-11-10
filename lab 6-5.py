#Author: edaddy 11/9/22
numbers = [4, 7, 8, 1, 5]
#creates list
if len(numbers) > 2:
#making the code executable by checking the amount of numbers
    numbers.sort ()
    #sorts the list from least to greatest
    print(numbers[-1])
    print (numbers[0])
else:
    print("error: list does not meet specifications!")