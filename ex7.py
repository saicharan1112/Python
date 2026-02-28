n1=float(input('Enter number1: '))
n2=float(input('Enter number2: '))

if abs(n1-n2)<=0.001:
    print('Close')
else:
    print('Not close')
