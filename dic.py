inventory={
    "apple":20,
    "grapes":40,
    "chickoo":30
}
#display
print(inventory)
#add stock
inventory["mango"]=15
print(inventory)
#del stock
inventory.__delitem__("apple")
print(inventory)
#using del
del inventory["grapes"]
print(inventory)


