highestnum = 0
# initialized highest num variable as 0
# will be replacing this 0 inside our for loop

for i in range(4): #could also write using 3 parameters range(0,4,1)
    userinput = input("\nNumber please...\n: ")
    userInt = int(userinput) #convert input string to int
    print("User entered: " + str(userinput)+"\n") #made sure the userinput converts to string to be printed
   
    #if statements checks and replaces highestnum with new user value if its greatr than highestnum 
    if userInt > highestnum:
        highestnum = userInt
        print("Updating highest number...\n")
    else:
        print("this is no the highest number!\n")

print("The largest number is : \n"+str(highestnum)+"\n")