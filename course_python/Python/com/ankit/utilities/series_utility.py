
def get_fibo_series(number):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(0,number-2):#n-2 bcoz last variable in loop is excluded.
        c=a+b
        print(c)
        a,b=b,c
    print('----------------------')
    return ' '

def get_even_series(number):
    i = 0
    while i<=number:
        if not i % 2:
            print(i)
        i = i+1
    print('----------------------')
    return ' '
    #pass # it signals Python system to ignore the empty block
    # if there is nothing in the funtion and we are using only pass the it will print none when we call it.
