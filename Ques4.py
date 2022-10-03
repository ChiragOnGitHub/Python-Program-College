def digits(num):
    a=set()
    while(num):
        a.add(num%10)
        num//=10
    return a

number=int(input("Enter the number: "))
print(digits(number))