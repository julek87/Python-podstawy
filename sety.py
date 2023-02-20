numbers_1 = {0, 1, 2, 4}
words = set(['ala', 'aga', 'julek'])

print(numbers_1)
print(words)

numbers_1.add(5)
numbers_1.remove(2)
print(numbers_1)
print(1 in numbers_1)
print(2 in numbers_1)

numbers_1 = {0, 1, 2, 4}
numbers_2 = {2, 3, 4, 5, 6}

print(numbers_1 | numbers_2)
print(numbers_1 & numbers_2)
print(numbers_1 - numbers_2)
print(numbers_1 ^ numbers_2)