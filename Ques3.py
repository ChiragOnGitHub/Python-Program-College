def fibonacci(n):
    if (n==1 or n==0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):
    product=1
    for i in range (1,n+1):
        product*=i
    return product

def main(n):
    l=[fibonacci(n-1),factorial(fibonacci(n-1))]
    return l


num=int(input("Enter the number : "))
print(main(num))