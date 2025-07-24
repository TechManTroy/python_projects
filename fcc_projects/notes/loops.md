### ✅ Save As: `python_loops.md`

# 🔁 Python Loops Reference

This document explains **loop types**, **control statements**, and **common tools** used in Python loops.

---

## 🌀 1. For Loops

Used to iterate over a sequence (like a list, string, or range).

```python
for item in iterable:
    print(item)
````

### 💡 Examples

```python
for char in 'hello':
    print(char)

for num in range(5):
    print(num)  # Outputs 0 to 4
```

---

## 🔄 2. While Loops

Repeats as long as a condition is `True`.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

> ⚠️ Be careful of infinite loops if the condition never becomes `False`.

---

## 🎛 3. Loop Control Statements

### 🔹 `break`

Stops the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### 🔹 `continue`

Skips the current iteration and moves to the next.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### 🔹 `pass`

Used as a placeholder when no action is needed.

```python
for i in range(3):
    pass  # Placeholder for future code
```

---

## 🧰 4. Useful Loop Tools

### 🔹 `range(start, stop, step)`

Generates a sequence of numbers.

```python
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9
```

### 🔹 `enumerate(iterable)`

Returns index and value while looping.

```python
words = ['apple', 'banana', 'cherry']
for index, word in enumerate(words):
    print(index, word)
```

### 🔹 `zip(list1, list2)`

Loops over multiple sequences in parallel.

```python
names = ['Alice', 'Bob']
scores = [90, 80]
for name, score in zip(names, scores):
    print(name, score)
```

---

## 📋 5. Nested Loops

A loop inside another loop.

```python
for i in range(3):
    for j in range(2):
        print(f'i={i}, j={j}')
```

---

## 🔍 6. Loop with Else

The `else` block runs **only if the loop didn't exit via `break`**.

```python
for i in range(3):
    print(i)
else:
    print("Loop completed without break")
```

---

## 🧠 7. Infinite Loop Example (with `while`)

```python
while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == 'exit':
        break
```

---

## ✅ Summary

| Type           | Usage Example              |
| -------------- | -------------------------- |
| `for` loop     | Loop through iterable      |
| `while` loop   | Loop until condition fails |
| `break`        | Exit loop early            |
| `continue`     | Skip this iteration        |
| `pass`         | Do nothing (placeholder)   |
| `range()`      | Create number sequences    |
| `zip()`        | Combine iterables          |
| `enumerate()`  | Loop with index            |
| `else` in loop | Runs if no `break`         |










