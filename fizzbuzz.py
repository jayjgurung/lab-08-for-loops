for counter in range(1,101):
    if (counter%3==0) & (counter%5==0): #question whats ther diff between and and && or &
        print("FizzBuzz")
    elif counter%3 == 0:
        print("Fizz")
    elif counter%5 ==0:
        print("Buzz")
    else:
        print(str(counter))