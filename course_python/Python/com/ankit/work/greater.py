'''
>= 70 - A
>= 60 - B
>= 40 - C
< 40 - F
> 100 or < 0 - I
'''
n = float(input ('Enter the marks to check GRADES: '))

if n >100 or n < 0:
    print('Invalid entry.')
elif n >=70:
   print('A Grade.')
elif n >=60:
   print('B Grade.')
elif n >=40:
   print('C Grade.')
else:
    print('F Grade.')
 