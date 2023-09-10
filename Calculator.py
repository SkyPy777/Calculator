while True:
    print("-----------------------------------------")
    print("\nOptions: ")
    print("\tAddition (add).")
    print("\tSubtraction (subtract).")
    print("\tMultiplication (multiply).")
    print("\tDivision (divide).")
    print("\tQuit")

    user_input = input("\nEnter the option: ")
    if user_input == 'quit':
         break
    if user_input in ("add", "subtract", "multiply", "divide"):
     num1 = float(input("Enter 1st number : "))
     num2 = float(input("Enter 2nd number : "))
     
     if user_input == 'add':
        result = num1 + num2
     elif user_input == 'subtract':
        result = num1 - num2
     elif user_input == 'multiply':
        result = num1 * num2
     elif user_input == 'divide':
        if num2 == 0:
            result = 'cannot divide by 0.'
        else:
           result = num1 / num2

     print("\nResult:",result)
    else:
        print("Invalid input! please try again.")

       
