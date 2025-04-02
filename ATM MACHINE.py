#Q3
balance=1000
print("\nATM MACHINE MENU=>\n1.check balance\n2.Deposit money\n3.withdraw money\n4.exit system")
ch=int(input("enter the choice"))
if(ch==1):
    print("your current balance is",balance)
elif(ch==2):
    deposit_money=int(input("enter amount to deposit"))
    balance+=deposit_money
    print("deposited successfully")
    print("new balance:",balance)
elif(ch==3):
    withdraw_money=int(input("enter amount to withdraw"))
    if( withdraw_money>balance):
        print("insufficient balance")
    else:
        balance-= withdraw_money
        print("new balance:",balance)
elif ch==4:
    print("thank you for using ATM machine")

else:
    print("invalid choice")

