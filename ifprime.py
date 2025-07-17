num = int(input("Enter the number: "))
isPrime = True

if num <= 1:
    isPrime = False
else:
    for i in range (2,num):
        if num%i==0:
            isPrime=false
if(isPrime):
    print("num is prime")
else:
    print("num is not prime")