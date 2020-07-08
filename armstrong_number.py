number = input("Enter a positive integer number:")
islem = 0

if number.isdigit(): 
    s_number = str(number)
    l_number = list(s_number)   
    ust = len(l_number) 
 
    for i in l_number :
        int_i = int(i)     
        islem += (int_i ** ust)     
    
    if int(number) == islem :
        print(f"{number} is an Armstrong number")
    else: 
        print(f"{number} is not an Armstrong number")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values")