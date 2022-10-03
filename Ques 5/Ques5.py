from fact import factorial

x=int(input("Enter the value of x : "))
n=int(input("Enter the value of n : "))

assert n>0,"Value of n must be greater than 0"

sum=0
for i in range(0,n+1,4):
    sum+=(x**i)/factorial(i)
for i in range(2,n+1,4):
    sum-=(x**i)/factorial(i)

print(sum)


