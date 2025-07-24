### 🔐 Vigenère Cipher (Intro Notes)

Unlike Caesar cipher, Vigenère uses a **key word** to vary the shift for each letter.

#### Setup:

```python
text = 'Hello Zaira'
custom_key = 'python'  # instead of using a fixed shift
```

#### 🔧 Function Definition:

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

#### 🚨 Common Mistake:

* Misspelling a variable name (`key_inder` instead of `key_index`)
* Using a variable (`offset`) before defining it (needs to be derived from `key_char`)

---

### ✅ Key Reminders:

* Always match variable names **inside and outside** the function.
* Define all variables before using them.
* Double check for typos, especially in loop counters or key logic.
* Vigenère cipher uses the **letter value from the key** as the shift.


