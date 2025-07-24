# 🐍 Common Python Built-in Functions

This document contains **frequently used built-in functions in Python**. Keep this handy as a quick reference while coding or building projects.

---

## 📄 String Functions

```python
str()         # Convert to string
len(string)   # Length of the string
ord('a')      # Unicode code of character
chr(97)       # Character from Unicode
````

---

## 🔢 Number Functions

```python
abs(x)        # Absolute value
round(x, n)   # Round to n decimal places
pow(x, y)     # x raised to power y (x ** y)
divmod(a, b)  # Returns (a // b, a % b)
sum(iterable) # Total of all values in iterable
min(iterable) # Smallest item
max(iterable) # Largest item
```

---

## 📋 Type Checking and Conversion

```python
type(x)         # Type of object
isinstance(x, T)# Check if x is instance of T
int(x)          # Convert to integer
float(x)        # Convert to float
str(x)          # Convert to string
bool(x)         # Convert to boolean
list(x)         # Convert to list
dict(x)         # Convert to dict
set(x)          # Convert to set
tuple(x)        # Convert to tuple
```

---

## 🛠 Utility Functions

```python
print(x)        # Output to console
input()         # Get user input as string
id(x)           # Memory address of object
dir(x)          # List all attributes of x
help(x)         # Show help/documentation
eval(expr)      # Evaluate expression from string
repr(x)         # Unambiguous string of object
bin(x)          # Binary representation
hex(x)          # Hexadecimal representation
oct(x)          # Octal representation
```

---

## 🧰 Functional Programming

```python
map(func, iterable)     # Apply function to each item
filter(func, iterable)  # Keep items where func(item) is True
zip(a, b)               # Combine multiple iterables
enumerate(iterable)     # Index and item pairs
sorted(iterable)        # Return sorted list
reversed(iterable)      # Return reversed iterator
any(iterable)           # True if any item is True
all(iterable)           # True if all items are True
```

---

## 🧪 Anonymous Functions

```python
lambda x: x * 2     # Quick one-line function
```

---

## 🧱 File I/O Functions

```python
open(filename, mode)    # Open a file
read(), readline(), write(), close()  # File object methods
```

> ⚠️ Always use `with open(...) as f:` for best practice.

---

## 🕓 Time & Date (Needs Import)

```python
import time
time.sleep(1)        # Pause for 1 second
time.time()          # Current time in seconds

import datetime
datetime.datetime.now()  # Current timestamp
datetime.date.today()    # Today's date
```

---

## ❗ Error Handling

```python
try:
    # risky code
except Exception as e:
    print(e)
finally:
    # always runs
```

---

## 🔍 Introspection & Debugging

```python
globals()     # Returns global symbol table
locals()      # Returns local symbol table
callable(x)   # Checks if x is callable (a function)
hasattr(obj, 'attr')  # Checks if object has attribute
getattr(obj, 'attr')  # Gets attribute from object
setattr(obj, 'attr', value)  # Sets attribute on object
```

---

## ✅ Summary

These are **essential Python functions** that will help you:

* Work with data
* Debug and explore your code
* Handle input/output
* Write cleaner and more efficient scripts



---




