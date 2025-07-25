# 🔐 Vigenère Cipher - Python Implementation and Documentation

---

## 📌 Overview

The **Vigenère Cipher** is a polyalphabetic substitution cipher that improves on the Caesar cipher by using a **keyword** to vary the shift for each letter in the message.

---

## 🧪 Input Example

```python
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'
```

* `text`: The encrypted message
* `custom_key`: The keyword used to shift each letter

---

## 🧠 Function Breakdown

### 🔧 Core Cipher Function

```python
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:        
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message
```

### 🔄 Purpose of Parameters

| Parameter   | Description                            |
| ----------- | -------------------------------------- |
| `message`   | The message to encrypt or decrypt      |
| `key`       | The keyword used for letter shifting   |
| `direction` | Set to `1` to encrypt, `-1` to decrypt |

---

### 🔐 Wrapper Functions

```python
def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)
```

* These helper functions allow for simpler usage of `vigenere()`.

---

## 🖨️ Usage Example

```python
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
```

---

## 📤 Sample Output

```
Encrypted text: mrttaqrhknsw ih puggrur
Key: happycoding

Decrypted text: hello zaira you rockstar
```

---

## ⚠️ Weaknesses of the Vigenère Cipher

| ❌ Weakness                              | 📄 Description                                                                                        |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Frequency analysis vulnerability**    | If the key is short or reused, frequency patterns emerge—susceptible to Kasiski and Friedman attacks. |
| **Easily brute-forced with short keys** | Modern tools can guess short keys quickly.                                                            |
| **Key must be shared securely**         | If someone intercepts the key, the whole system is compromised.                                       |
| **Only handles alphabetic characters**  | You’d need to modify the cipher to support digits, punctuation, or unicode.                           |
| **Outdated by modern standards**        | Offers no real security today—modern encryption like AES is recommended.                              |

---

## ✅ Final Thoughts

The Vigenère Cipher is an excellent tool for learning encryption principles and working with strings and loops in Python. But it should **never be used for securing real-world data**.



