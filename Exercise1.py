


for loopCounter in range(5):
    print(loopCounter)



userInput = input("What would you like to type in? ")

def userPrint():
    for loopCounter in range(2):
        print (userInput)


userPrint()




def userNumberFunction():
    userNumber = int(input("Enter a number between 1 and 10? "))
    if (userNumber < 11):
        print(userNumber)

userNumberFunction()



def whileLoopCounter():
    userNumberInput = int(input("What number would you like to input? "))
    while (userNumberInput != 0):
        print(userNumberInput)
        break

whileLoopCounter()



def whileLoopPrint():
    userNumberInput2 = (input("Enter the number 1, 2, 3, or 0: "))
    while (userNumberInput2 != "0"):
        if (userNumberInput2 == "1"):
            print("1")
            break
        elif (userNumberInput2 == "2"):
            print("2")
            break
        elif (userNumberInput2 == "3"):
            print("3")
            break
        elif (userNumberInput2 == "0"):
            break
        else:
            print("ERROR")
            break



whileLoopPrint()

userNumberInput3 = input("Enter a number between 1 and 3 or q to quit: ").lower()

def one():
    while (userNumberInput3 != "q"):
        if (userNumberInput3 == "1"):
            print("1")
            break

def two():
    while (userNumberInput3 != "q"):
        if (userNumberInput3 == "2"):
            print("2")
            break


def three():
    while (userNumberInput3 != "q"):
        if (userNumberInput3 == "3"):
            print("3")
            break

def quit():
        if(userNumberInput3 != "1" and userNumberInput3 != "2"
                and userNumberInput3 != "3" and userNumberInput3 != "q" ):
            return ("Error")


def allTogether():
    if (userNumberInput3 == "1"):
        one()
    elif(userNumberInput3 == "2"):
        two()
    elif(userNumberInput3 == "3"):
        three()
    elif(userNumberInput3 == "q"):
        print("Project terminated")
    else:
        print(quit())


allTogether()