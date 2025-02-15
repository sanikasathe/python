balance=1000
print("current balance",balance)
withdraw=int(input("enter amount"))
if(withdraw%10!=0):
    print("error")
elif(withdraw>balance):
    print("insufficient balance")
else:
    print("withdraw successful",withdraw)
    print("remaining balance",balance-withdraw)
