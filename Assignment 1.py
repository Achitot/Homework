#Creating a List
fruits = ['strawberry', 'mango', 'avocado', 'papaya']
print(fruits)

# Accessing Elements
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print ('First color: ', colors [0])
print ('Third color: ', colors [2])
print ('Last color: ', colors [-1])

# Modifying a List
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
numbers.append(60)
print (numbers)

# List Slicing
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[:3]
print (subset)

# Looping through a List
num1 = list(range(1, 11))
for num2 in num1:
    print(f"{num2} squared is {num2 ** 2}")

# Append and Extend
shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.extend(['butter', 'cheese'])
print (shopping_cart)

# Finding Maximum and Minimum in a List
numbers = [45, 22, 88, 56, 92, 33]
print ('Maximum number:', max(numbers))
print ('Mininmum number:', min(numbers))

# Counting Occurrences
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
counts = letters.count('a')
print ('Count of a:', counts)

# List Comprehension
squared_evens = [num ** 2 for num in range(0, 11) if num % 2 == 0]
print("Squares of even numbers from 0 to 10:", squared_evens)

# Removing Duplicates
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
remove = sorted(list(set(nums)))
print (remove)

single = []
for num in nums:
    if nums.count(num) == 1:
        single.append(num)
print (single)

#Comment