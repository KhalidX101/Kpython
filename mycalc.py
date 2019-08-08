#KHALID DID THIS HURRAY!!!!!!!!!!!!!!!!!!
'''This is calculator for your handy and simple mathematics by khalid
thanks! .'''
while True:
    def calculator(firstdigit,seconddigit,operator):
        try:
            if operator == "Addition":
                result = firstdigit + seconddigit
                return result

            # For Multiplication

            elif operator == "Multiplication":
                result = firstdigit * seconddigit
                return result

            # For Subtraction
            elif operator == "Subtraction":
                result = firstdigit - seconddigit
                return result

            #For Division
            elif operator =="Division":
                result = firstdigit / seconddigit
                return result

            #For Remainder
            elif operator == "Reminder":
                result = firstdigit % seconddigit
                return result

            else:
                print("WRONG INPUT PLEASE ++++++++++++ TRY AGAIN")
        except Exception:
            print('Wrong Calculation Error')


#ALL THE METHOD CALL IN THIS CODE KHALID
    print("Welcome to My Calculator By Khalid\n \t\t\t Calculate \t\t\t \n")
    var=input('what is the first digit: ')
    var1=input('what is the second digit: ')
    var2=input('what is the operation: ')
    result=calculator(float(var),float(var1),var2)
    print("The Result for the " + var2 + " is " + str(result))
    Answer=input("\n Do you want to continue (y/n): ")
    if Answer == "y":
        continue
    else:
        break


