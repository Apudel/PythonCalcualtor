
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b


def Divide(a, b):
    return a / b


menu=" "
while(menu != "E" or menu != "e"):
    print("===================================")
    print("------------Calculator-------------")
    print("----------Made By Atulya-----------")
    print("===================================")
    print("Choose From The Following Options:-")
    print("(1)Addition")
    print("(2)Substraction")
    print("(3)Multiplicaition")
    print("(4)Division")
    print("(E)Exit")
    print("===================================")
    menu = input("Enter Your Option:- ")
    if(menu == "1"):
        print("===================================")
        Numb1 = float(input("Enter First Number:- "))
        Numb2 = float(input("Enter Second Number:- "))
        print("===================================")
        print("The Sum Of", Numb1, "And", Numb2, "is", add(Numb1, Numb2))
        print("===================================")

    elif(menu == "2"):
        print("===================================")
        Numb1 = float(input("Enter First Number:- "))
        Numb2 = float(input("Enter Second Number:- "))
        print("===================================")
        print("The Difference Of", Numb1, "And", Numb2, "is", sub(Numb1, Numb2))
        print("===================================")

    elif(menu == "3"):
        print("===================================")
        Numb1 = float(input("Enter First Number:- "))
        Numb2 = float(input("Enter Second Number:- "))
        print("===================================")
        print("The Product Of", Numb1, "And", Numb2, "is", multiply(Numb1, Numb2))
        print("===================================")

    elif(menu == "4"):
        print("===================================")
        Numb1 = float(input("Enter First Number:- "))
        Numb2 = float(input("Enter Second Number:- "))
        print("===================================")
        if(Numb1 == 0 or Numb2 == 0 ):
            print("===================================")
            print("Math Error")
            print("===================================")
            input("Press Enter To Try Again ")
            print("===================================")
        else:
            print("===================================")
            print("The Quotient Of", Numb1, "And", Numb2, "is", Divide(Numb1, Numb2))
            print("===================================")

    elif (menu== "e" or menu== "E"):
        print("===================================")
        print("Program Closed!")
        print("===================================")
        break
    else:
       print("Invalid Operation!")
       print("===================================")
    input("Press Enter To Continue Calculations Or To Exit!")
    print("===================================")