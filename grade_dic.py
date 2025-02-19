students_grade={
    "pranali":"A",
    "prachi":"B",
    "Snehal":"C",
    "gouri":"D"
}
#DISPLAY GRADE
print(students_grade)
#add 
students_grade["sanika"]="A+"
print("after insertion",students_grade)
#deletion
students_grade.__delitem__("Snehal")
print("after deletion",students_grade)
#update
students_grade.update({"gouri":"C+"})
print("after UPDATING",students_grade)




