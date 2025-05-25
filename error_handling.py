is_running = True


while is_running:
    try:
        choice1 = int(input("Enter the first number :"))
        choice2 = int(input("Enter the second number :"))

        if choice2 == 0:
            print("Cannot divide by zero")

        else:  
            result = choice1/choice2
            is_running = False  

    except ValueError:
        print("Please enter valid integers")



print("Result :",result)        
    