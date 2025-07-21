### 📝 **Note: Variable Scope in Functions (Python)**

**Topic:** Why `print(encrypted_text)` didn't work outside my function

---

#### ✅ Problem I Had:

I defined `encrypted_text` **inside** my function `caesar()`, but tried to use it **outside** the function. Python gave me this error:

```bash
NameError: name 'encrypted_text' is not defined
```

---

#### 🎯 Why That Happened:

In Python, **variables created inside a function only exist inside that function**. This is called **local scope**.

So if I do this:

```python
def caesar():
    encrypted_text = 'something'
```

Then try to do:

```python
print(encrypted_text)  # ❌ This will cause an error
```

It won’t work because `encrypted_text` is not visible **outside** the `caesar()` function.

---

#### ✅ How I Fixed It:

I moved the `print()` statements **inside the function** like this:

```python
def caesar():
    encrypted_text = 'something'
    print(encrypted_text)  # ✅ This works

caesar()  # Call the function so it runs
```

---

#### 📌 Future Tip:

If I ever want to use a variable **outside** the function, I’ll eventually need to learn about `return`, like this:

```python
def caesar():
    return 'something'

result = caesar()
print(result)
```

(But I haven’t learned that in freeCodeCamp yet!) 07/21/2025
