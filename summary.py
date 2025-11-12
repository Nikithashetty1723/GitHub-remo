| Category           | Examples                           |
| ------------------ | ---------------------------------- |
| **Basic Syntax**   | Indentation, comments              |
| **Data Types**     | int, float, str, list, tuple, dict |
| **Control Flow**   | if, for, while                     |
| **Functions**      | def, return, lambda                |
| **OOP**            | class, self, init                  |
| **Modules**        | import, from                       |
| **Error Handling** | try, except                        |
| **File I/O**       | open(), read(), write()            |

python syntax:

# Comments
# Single line comment
"""
Multi-line comment
"""

# Variables and Data Types
x = 10              # int
name = "Nikki"      # string
pi = 3.14           # float
is_active = True    # boolean
colors = ["red", "blue"]   # list
person = {"name": "Nikki", "age": 25}  # dictionary

# Conditional Statements
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Loops
for i in range(5):
    print(i)

count = 0
while count < 3:
    print(count)
    count += 1

# Functions
def greet(name):
    return "Hello " + name

print(greet("Nikki"))

# Class and Object
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am", self.name)

p = Person("Nikki")
p.say_hi()

# Try / Except (Error Handling)
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
finally:
    print("Done")

# Input and Output
name = input("Enter your name: ")
print("Hello", name)

# Operators
# +, -, *, /, %, **, //, ==, !=, >, <, >=, <=, and, or, not, in, is

# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)

# File Handling
with open("file.txt", "r") as f:
    print(f.read())

# Lambda Function
add = lambda a, b: a + b
print(add(3, 4))

# Import Modules
import math
print(math.sqrt(16))
