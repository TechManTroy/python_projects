### 🔐 Vigenère Cipher (Intro Notes)

Unlike Caesar cipher, Vigenère uses a **key word** to vary the shift for each letter.

---

### ✍️ Setup:

```python
text = 'Hello Zaira'
custom_key = 'python'  # instead of using a fixed shift
```

---

### 🔧 Function Definition:

```python
def vigenere(message, key):
    key_index = 0  # To loop through the key repeatedly
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            key_char = key[key_index % len(key)]  # Repeat key as needed
            key_index += 1

            # Calculate shift based on the key character
            offset = alphabet.find(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    print('plain text:', message)
    print('encrypted text:', encrypted_text)
```

---

### 🚀 Calling the Function:

```python
encryption = vigenere(text, custom_key)
```

---

### 🚨 Common Mistakes:

* ❌ Misspelling a variable name (`key_inder` instead of `key_index`)
* ❌ Using a variable before defining it (`offset` from `key_char`)
* ❌ Using a wrong function name when calling it (e.g., `vingenere` instead of `vigenere`)

---

### ✅ Key Reminders:

* Always match variable names **inside and outside** the function.
* Define all variables before using them.
* Double-check for typos, especially in loop counters or key logic.
* Vigenère cipher uses the **letter value from the key** as the shift.
* The key loops repeatedly through the text.

---

### 🧠 Example Output:

```text
plain text: Hello Zaira
encrypted text: wjcpa niyvp
```

---

### 📁 Notes File Usage

This .md file expands on Caesar cipher notes by introducing:
- Key-based letter shifting
- Repeating keys
- Common debugging techniques for classical ciphers

Good for: **cipher comparison, debugging patterns, and Python string logic practice.**

📌 📘 Expansion – What I Learned Today: 07/23/2025

✅ I learned how to use the return statement in a Python function.
    Instead of printing the result directly from inside the function, I now return it to use later.

✅ I learned how to call a function using two arguments: the message and the key.
```    
Example: vigenere(text, custom_key)
```
✅ I learned how to store the result of a function in a variable.
 I stored the encrypted result in a variable called encryption, like this:

```
encryption = vigenere(text, custom_key)
print(encryption)  # Output the returned value
```

✅ This helps keep my code more flexible, clean, and reusable.

