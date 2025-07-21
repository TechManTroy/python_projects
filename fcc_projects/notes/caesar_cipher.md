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

### 📁 Caesar Cipher Debugging Tips (Beginner Python)

**Goal:** Encrypt a message using a Caesar cipher.

---

### 🔐 Key Things to Remember

1. **Define variables before using them**

   * Make sure `text` and `shift` are defined **before** the loop or function that uses them.

2. **Indentation matters!**

   * Python uses indentation to group code. Anything that belongs inside the function (or loop) must be indented properly.

3. **Use `.lower()` when matching characters**

   * This ensures your text matches the lowercase alphabet you're using for encryption.

4. **Make sure `print()` statements are inside the function (if you want them to run when the function is called)**

   * If you define `print()` outside the function, they won't have access to variables like `encrypted_text` that are created inside the function.

5. **Call the function!**

   * Just defining `def caesar():` doesn't run the code inside. You must call it later with `caesar()`.

---

### ❌ Common Mistake I Made

> I placed the `print()` statements **outside** of the function, so the program didn't know what `encrypted_text` was when trying to print it.

**Fix:** Move the `print()` lines **inside** the function block.

---

### ✅ Correct Structure (No Extra Concepts):

```python
text = 'Hello Zaira'
shift = 3

def caesar():
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ''

  for char in text.lower():
    if char == ' ':
      encrypted_text += char
    else:
      index = alphabet.find(char)
      new_index = (index + shift) % len(alphabet)
      encrypted_text += alphabet[new_index]

  print('plain text:', text)
  print('encrypted text:', encrypted_text)

caesar()
```

---



