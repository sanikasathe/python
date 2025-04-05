#Q7
amount=int(input("enter the amount(multiple of 500)"))
#CALCULATE NUMBER OF 2000
count_0f_2000rs=amount//2000
remaining_amount=amount%2000
#CALCULATE NUMBER OF 500
count_0f_500rs=remaining_amount//500

#DISPLAY THE RESULT
print("for rs",amount)
print("we need",count_0f_2000rs,"note of 2000")
print("we need",count_0f_500rs,"note of 500")





