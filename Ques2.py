def sales(w1,w2,w3,w4):
    totalSale=w1+w2+w3+w4
    if totalSale>50000:
        commission=totalSale/20
    else:
        commission=0

    if totalSale>=80000:
        remark="Excellent"
    elif 60000<=totalSale<80000:
        remark="Good"
    elif 40000<=totalSale<60000:
        remark="Average"
    else:
        remark="Work Hard"
    t1=(totalSale,commission,remark)
    return t1

def main():
    salesMan=int(input("Enter number of salesman : "))
    for i in range(salesMan):
        print()
        print("Enter sales of salesman ",i+1)
        week1=float(input("Enter sale for week 1 : "))
        week2=float(input("Enter sale for week 2 : "))
        week3=float(input("Enter sale for week 3 : "))
        week4=float(input("Enter sale for week 4 : "))

        t=sales(week1,week2,week3,week4)
        print()
        print("Total sales of Sales Man ",i+1,": ",t[0])
        print("Commission of Sales Man ",i+1,": ",t[1])
        print("Remark of Sales Man ",i+1,": ",t[2])

main()