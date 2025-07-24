# 🔐 Caesar Cipher - Python Implementation and Documentation

---

## 📌 Overview

The **Caesar Cipher** is a simple substitution cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet. It’s one of the oldest known encryption techniques.

---

## 🧪 Input Example

```python
# Original message to encrypt
text = 'Hello Zaira'

# Number of positions to shift each letter
shift = 3
```

* `text`: The message to encrypt.
* `shift`: The number of positions each letter is shifted (e.g., a shift of `3` turns `a` into `d`).

---

## 🧠 Caesar Cipher Function

```python
def caesar(message, offset):
    # Define the alphabet used for the cipher
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Initialize the encrypted text variable
    encrypted_text = ''
```

* `alphabet`: The lowercase letters of the English alphabet used for reference.
* `encrypted_text`: Used to build the result string letter-by-letter.

---

### 🔁 Encrypting the Message

```python
    for char in message.lower():
```

* Converts the entire message to lowercase so it matches the `alphabet`.

```python
        if char == ' ':
            encrypted_text += char
```

* Keeps spaces unchanged for readability.

```python
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
```

* `index`: Finds the position of the character in the alphabet.
* `new_index`: Adds the shift (`offset`) and wraps around using modulo.
* Appends the new letter at `new_index` to `encrypted_text`.

---

### 🖨️ Output Results

```python
    print('plain text:', message)
    print('encrypted text:', encrypted_text)
```

* Displays both the original and encrypted versions of the message.

---

## ✅ Function Call and Variable Assignments

```python
# Assign values to the variables used in function call
text = message     # Assign the original message to a new variable 'text'
shift = offset     # Assign the original offset to a new variable 'shift'

# Call the function using new variable names
caesar(text, shift)
```

* `text` and `shift` are now reused to make the function call more intuitive.

---

## 🔁 ROT13 - Common Caesar Variant

```python
# Call the function again using a fixed Caesar shift of 13 (ROT13 encryption)
caesar(text, 13)
```

* **ROT13** is a variation of the Caesar cipher where each letter is rotated 13 places.
* It is symmetric: encrypting and decrypting are the same.

---

## ❗ Weaknesses of the Caesar Cipher

| ❌ Weakness                     | 📄 Description                                                              |
| ------------------------------ | --------------------------------------------------------------------------- |
| **Very easy to break**         | Only 25 possible shifts. Can be brute-forced in seconds.                    |
| **No key management**          | If someone knows the method, the shift is trivial to guess.                 |
| **Frequency analysis**         | Letter frequency stays the same, making it vulnerable to pattern detection. |
| **No case or symbol handling** | Only lowercase letters are used here—no punctuation, numbers, or symbols.   |

---

## ✅ Final Thoughts

The Caesar Cipher is an excellent introductory exercise for learning about:

* **Loops**
* **Modulus arithmetic**
* **String manipulation**

However, **it is not secure** and only useful for teaching or puzzles—not for real-world applications.




