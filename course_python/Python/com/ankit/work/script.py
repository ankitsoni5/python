def area(length, breadth):
    a = length * breadth
    return a

def perimeter(length, breadth):
    p = 2 * (length + breadth)
    return p

l = float(input ('Enter lenght: '))
b = float(input ('Enter breadth: '))

p = area(l,b)
q = perimeter(l,b)

print (p)
print (q)