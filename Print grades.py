#Q13
#FUNCTION DEFINING
def students_grade():
       marks=int(input("enter the students marks"))
       if(90<=marks<=100):
              print("Grade:A")
       elif(80<=marks<=89):
              print("Grade:B")
       elif(70<=marks<=79):
              print("Grade:C")
       elif(60<=marks<=69):
              print("Grade:D")
       else:
            print("Grade:F")

#CALLING FUNCTION
students_grade()
