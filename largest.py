highestnum = 0
# initialized highest num variable as 0
# will be replacing this 0 inside our for loop

for i in range(0,4,1):
    userinput = input("\nNumber please...\n: ")
    userInt = int(userinput)
    print("User entered: " + str(userinput)+"\n")
    if userInt > highestnum:
        highestnum = userInt
        print("Updating highest number...\n")
    else:
        print("this is no the highest number!\n")
print("The largest number is : \n"+str(highestnum)+"\n")