sum = 0
for count in range(4):
    userInput = input("\nNumber please ..\n")
    sum = int(sum) + int(userInput)
average = sum/4
print("\nThe average is : \n" + str(average) + "\n")
