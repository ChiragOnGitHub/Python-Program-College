def Triangle(): 
    side1=int(input("Enter length of side 1 of triangle : "))
    side2=int(input("Enter length of side 2 of triangle : "))
    side3=int(input("Enter length of side 3 of triangle : "))

    assert side1+side2>side3 and side2+side3>side1 and side3+side1>side2 , "Triangle is invalid!!"

    perimeter=side1+side2+side3
    s=(side1+side2+side3)/2
    area=(s*(s-side1)*(s-side2)*(s-side3))**0.5

    return area,perimeter

print("Tuple of area and perimeter :",Triangle())