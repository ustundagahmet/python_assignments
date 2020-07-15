fibonacci = []

for i in range(1, 10) :
    if i == 1 :
        fibonacci.append(1)
        fibonacci.append(1)
    elif i > 1 :
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])

print(fibonacci)