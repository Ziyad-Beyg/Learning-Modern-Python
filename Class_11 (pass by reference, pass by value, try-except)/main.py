""" 
In Python every thing is an Object. 
There are two major datatypes:
1) Mutable Datatypes : One who's value can be updated.
2) Immutable Datatypes : One who's value can not be updated.

Mutable Types include => (Dictionary, List, Set)
Immutable Types include => (Integers, Floats, Strings, and Tuples)

In Python if we pass num1 variable that is immutable to num2 variable, num1's value will be passed as reference to num2 and both variable will share same memory address as the value/data is same(no need to store same data twice). But if we increased the value of num2 by 1, because num2 is immutable it will create a new object with new memory address for the data. However in mutable types we can update the reference value but in result the original object is also altered. 
"""

number : int = 10
number2 : int = number

print(f"Num1 : {number}, Num2: {number2}")
print(f"Num1 Address : {id(number)}, Num2 Address: {id(number2)}")

number2 += 2

print(f"Num1 : {number}, Num2: {number2}")
print(f"Num1 Address : {id(number)}, Num2 Address: {id(number2)}")
