f=int(input('Enter length in feet:'))
while True:
    print('1. Inches')
    print('2. Yards')
    print('3. Miles')
    print('4. Millimeters')
    print('5. Centimeters')
    print('6. meters')
    print('7. Kilometers')
    print('8. Exit')
    a=int(input('Enter your choice:'))
    while True:
        if a<=8:
            break
        else:
            a=int(input("Enter correct number:"))
            if a<=8:
                break
    if a==1:
        r=f*12
    elif a==2:
        r=f/3.0
    elif a==3:
        r=f/5280.0
    elif a==4:
        r=f*304.8
    elif a==5:
        r=f*30.48
    elif a==6:
        r=f*0.3048
    elif a==7:
        r=f*0.0003048
    elif a==8:
        break
    print('The required result=',r)

