n = int(input('Enter the number till you want to print: '))
a,b =0,1
print(a)
print(b)
'''
With While Loop

i = 0
while i<=n-3:
    c=a+b
    print(c)
    a,b=b,c
    i = i+1

END
'''
# Using For Loop
for i in range(0,n-2):#n-2 bcoz last variable in loop is excluded.
    c=a+b
    print(c)
    a,b=b,c