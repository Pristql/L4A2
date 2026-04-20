W=int(input("Enter your desired withdrawal amount: "))

a=W//100
b=(W%100)//50
c=((W%100)%50)//10

print("notes of 100 rupees: ", a)
print("notes of 50 rupees: ", b)
print("notes of 10 rupees: ", c)