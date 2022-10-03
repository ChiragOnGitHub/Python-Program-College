def evenElements(t1):
    l=[]
    for i in t1:
        if i%2==0:
            l.append(i)
    t=tuple(l)
    return t

def concatination(t1,t2):
    t3=t1+t2
    return t3
    
def maxMin(t):
    max=min=t[0]
    for i in t:
        if(i>max):
            max=i
        elif(i<min):
            min=i
    return max,min

def main():
    t1=(1,2,5,7,9,2,4,6,8,10)

    t2=evenElements(t1)
    print("Tuple with even elements is : ",t2)

    t3=(11,13,15)
    t1=concatination(t1,t3)
    print("Tuple 1 after concatination : ",t1)

    max,min=maxMin(t1)
    print("Maximum element in tuple 1 is : ",max)
    print("Minimum element in tuple 1 is : ",min)

main()