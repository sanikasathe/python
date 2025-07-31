num=int(input("enter the number"))
sum_of_powers=0
original_num=num
while num>0:
    digit=num%10
    sum_of_powers+=digit**3
    num//=10
if(sum_of_powers==original_num):
    print(f"{original_num} is a armstrong number")
else:
    print(f"{original_num} is not armstrong number")


