'''
1. Fibo Series
2. Even Series
3. Even Odd
4. Exit
Repete until user exits.

'''
import com.ankit.utilities.series_utility #This just import the module not the function
import com.ankit.utilities.math_utility

'''TO import the function rather then importing full module
from math_utility import get_even_odd  here we can directly use the function without using module name

We can also remane the function for the current file like:
from math_utility import get_even_odd as evenseries

So here we can use get_even_odd as evenseries for this file
'''

while True:
    #print('1. Fibo Series\n2. Even Series\n3. Even Odd\n4. Exit') 
    print('1. Fibo Series', '2. Even Series', '3. Even Odd', '4. Exit' , sep='\n') # can be written in both way
    n = int(input('Please enter the choice: '))

    if n==4:
        break
    
    if n==1 or n==2 or n==3:
        number = int(input('Please enter the number: '))

    if n == 1:
        print(com.ankit.utilities.series_utility.get_fibo_series(number))
    elif n==2:
        print(com.ankit.utilities.series_utility.get_even_series(number))
        
    elif n==3:
        print(com.ankit.utilities.math_utility.get_even_odd(number))
    else:
        print('Invalid Option.')
        print('----------------------')
    



