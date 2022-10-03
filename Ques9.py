def average(d):
    count=0
    for i in d:
        if count==0:
            highest=i
            count+=1
        elif (d[i]["sub1"]+d[i]["sub2"]+d[i]["sub3"]+d[i]["sub4"])/4 > d[highest]["sub1"]+d[highest]["sub2"]+d[highest]["sub3"]+d[highest]["sub4"]/4:
            highest=i
    return highest

d={}
while(True):
    print()
    print("Press 1 to Enter the detail of student ")
    print("Press 2 to Find the name of the student securing highest percentage :")
    print("Press Any Other Key to Quit")
    print()

    choice = int(input("Enter you choice : "))

    if choice == 1:
        name=input("Enter name of the Student ")
        if name in d:
            print("This student already exist !!")
        else:
            sub1=float(input("Enter marks of subject 1 : "))
            sub2=float(input("Enter marks of subject 2 : "))
            sub3=float(input("Enter marks of subject 3 : "))
            sub4=float(input("Enter marks of subject 4 : "))
            d[name]={"sub1":sub1,"sub2":sub2,"sub3":sub3,"sub4":sub4}
            print("Record of the student updated successfully!! ")

    elif choice == 2:
            print("Highest Average marks is sceured by ",average(d))

    else:
        break

