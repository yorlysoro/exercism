from array import array

array1 = array('i', [1, 2, 3, 4, 5])

for x in array1:
    print(x)

print(array1[0])
print(array1[4])

array1.insert(1, 6)

print(array1)

array1.remove(3)

print(array1)

print(array1.index(4))

array1[2] = 7

print(array1)
