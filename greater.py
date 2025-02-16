num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
num3=int(input("enter 3rd number"))
if(num1>num2):
    if(num1>num3):
        print("num1 is greater")
    else:
        print("num3 is greater")
elif(num2>num3):
    print("num2 greater")
else:
    print("num3 greater")  
