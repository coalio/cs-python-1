# You can use this file as a reference for writing your tests

"""
Test 1. Calculate the factorial of a number
"""

from tests.factorial import factorial

print(factorial(int(input("Enter a number: "))))

"""
Test 2. Calculate the fibonacci sequence up to N
"""

from tests.fibonacci import fibonacci

n = int(input("Enter a number: "))
print([fibonacci(N) for N in range(n)])

"""
Test 3. Make a list
"""
array = []
for N in range(int(input("How many elements: "))):
    array.append(input("Enter str: "))

for index in range(len(array)):
    # Print all elements
    print(f"Element {index}: ", array[index])

"""
Test 4. Students
"""
from projects import main # This should execute it
