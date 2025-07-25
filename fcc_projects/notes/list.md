# 🧪 Python List Exploration

This short script demonstrates how to work with **Python lists** using common methods like `append()`, indexing, assignment, `insert()`, and `pop()`.

---

## 📜 The Code (With Comments)

```python
# Create a list with two initial elements
my_list = [1, 2]

# Append the number 3 to the end of the list
my_list.append(3)
print(my_list)  # Output: [1, 2, 3]

# Print the first element (index 0) of the list
print(my_list[0])  # Output: 1

# Change the value of the first element to 0
my_list[0] = 0
print(my_list)  # Output: [0, 2, 3]

# Insert the number 1 at index 1
my_list.insert(1, 1)
print(my_list)  # Output: [0, 1, 2, 3]

# Remove and return the last element of the list
my_list.pop()
print(my_list)  # Output: [0, 1, 2]
````

---

## 🧠 What You Learned

### ✅ 1. `append()`

* Adds an element to the **end** of a list.

```python
my_list.append(3)  # -> [1, 2, 3]
```

### ✅ 2. Indexing

* You can access specific elements using their index:

```python
my_list[0]  # -> 1
```

### ✅ 3. Assignment

* You can change the value of a specific element by index:

```python
my_list[0] = 0  # -> [0, 2, 3]
```

### ✅ 4. `insert(index, value)`

* Inserts an element at a specific position, pushing the rest forward:

```python
my_list.insert(1, 1)  # -> [0, 1, 2, 3]
```

### ✅ 5. `pop()`

* Removes the **last** element by default:

```python
my_list.pop()  # -> removes 3, resulting in [0, 1, 2]
```

---

## 📌 Summary

Python lists are **mutable**, ordered collections that allow:

* Dynamic changes (adding, inserting, removing elements),
* Direct access by index,
* And flexible manipulation using built-in methods.

They are one of the most versatile and widely used data structures in Python.

