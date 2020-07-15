number = int(input("Enter a number:"))
count = 0

for i in range(1, number+1):
    if number % i == 0:
        count += 1

if number == 0 or number == 1 or count >= 3:
        print(number, "is not a prime number")

else:
    print(number, "is  a prime number")
