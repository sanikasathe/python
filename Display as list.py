#Q8
list=[]
item=""
while True:
    item=str(input("enter item: "))
    if item!="done":
        list.append(item)
    else:
        print(list)
        break


