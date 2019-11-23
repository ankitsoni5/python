print('program Starts.')

while True:
    i = input('Enter n: ')
    try:# try to keep only those statement in try block which can create exception.
        n = int(i)
    except ValueError:
        print('Please pass an integer value.')
    else:
        # will execute when there is no exception in try block or is a success
        print('odd') if n % 2 else print('Even')
        break


print('Program Ends.')