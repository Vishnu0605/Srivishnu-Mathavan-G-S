print("Welcome to the Calculater")

Call=True
while Call:

    A=int(input("\nEnter the value of A:"))
    choice=input("Enter your choice(+,-,*,/):")
    B=int(input("Enter the value of B:"))

    if choice=='+' :
        C=A+B
        print(f"The Addition of the {A}+{B} is :",C)
     
    elif choice=='-' :
        C=A-B
        print(f"The Subtraction of the {A}-{B} is :",C)

    elif choice=='*' :
        C=A*B
        print(f"The Multiplication of the {A}*{B} is :",C)

    elif choice=='/' :
        C=A/B
        print(f"The Division of the {A}/{B} is :",round(C,2)) 
        
    else :
        print("Enter the correct choice")
