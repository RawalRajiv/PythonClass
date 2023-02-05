'''
---------------------------------------------------------------------------------------
This is example of While, User input, If elif else as well as Try Catch exception
---------------------------------------------------------------------------------------
'''
while True:
    userValue = input("Please enter raw value:");
    try:
        userInputValue = int(float(userValue))
        if(userInputValue <=0):
            raise ValueError
        elif userInputValue >= 91:
            print("A+ Grade")
        elif userInputValue < 91 and userInputValue >= 75:
            print("A Grade")
        elif userInputValue < 75 and userInputValue >= 60:
            print("B Grade")
        elif userInputValue < 60 and userInputValue >=50:
            print("C Grade")
        elif userInputValue < 50 and userInputValue >= 35:
            print("D Grade")
        else:
            print("F Grade")
        break
    except ValueError:
        print("Kindly key in proper value")
