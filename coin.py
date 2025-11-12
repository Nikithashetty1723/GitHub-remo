What is a Comment?
A comment is text written in code that Python ignores when running.
It’s just for humans to understand the logic, purpose, or notes about the code.
Think of it like writing sticky notes inside your program 📝 — they help you and others understand what’s happening.

🧠 Why Comments Are Important
Explain what your code does
Help others understand your logic
Remind your future self why you wrote something
Debug or temporarily disable a piece of code



🔹 Types of Comments in Python

✅ 1. Single-line Comment
Starts with a # (hash) symbol.
Everything after # is ignored by Python.
# This is a single-line comment
x = 10  # Assigning 10 to variable x

✅ 2. Multi-line Comment
Python doesn’t have a special syntax for multi-line comments like other languages (/* ... */),
but you can use triple quotes (''' or """) to write text that looks like multi-line comments.
"""
This is a multi-line comment
You can write notes here
Python will ignore this
"""

🔸 Triple quotes are mostly used for docstrings (documentation for functions or classes),
but can also act as long comments.

✅ 3. Docstrings (Documentation Strings)
Docstrings are special multi-line comments that explain what a function or class does.
They are not ignored — they’re stored as documentation and can be accessed using help().
def greet(name):
    """This function greets the person passed as argument."""
    print("Hello", name)

help(greet)

Output:
Help on function greet in module __main__:
greet(name)
    This function greets the person passed as argument.




🧱 2️⃣ Indentation in Python:::


💡 What is Indentation?
Indentation means spaces at the beginning of a line.
In Python, indentation shows which lines belong together (like inside an if, loop, or function).
Unlike other languages (like C or Java) that use {} braces,
Python uses indentation to define code blocks.

🧠 Example
if True:
    print("Hello")
    print("World")
print("Outside block")

Output:
Hello
World
Outside block

If you remove indentation:
if True:
print("Hello")   # ❌ Error: expected an indented block

Python will give an IndentationError.

🔹 Rules for Indentation


Use 4 spaces per indentation level (recommended by PEP 8).


Be consistent — don’t mix spaces and tabs.


Each block inside if, for, while, def, class, etc., must be indented.



✅ Examples
Function Example
def greet():
    print("Hello")       # Inside function
    print("Welcome!")    # Inside function
print("Bye")             # Outside function

Loop Example
for i in range(3):
    print(i)
    if i == 2:
        print("End of loop")


⚠️ Common Errors
❌ Mixing tabs and spaces:
if True:
⇥print("Hello")   # (Tab)
    print("Hi")   # (Spaces)

➡️ Will cause TabError: inconsistent use of tabs and spaces in indentation


✅ Comments → for humans
✅ Indentation → for Python to understand structure


