import random
print("Random number generator")
count=int(input("how many number you want to generate?"))
start=int(input("Enter starting number of range: "))
end=int(input("Enter ending number of range: "))
print("\n Generated random numbers: ")
for i in range(count):
    number=random.randint(start,end)
    print(number)

