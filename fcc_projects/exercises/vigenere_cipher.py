# Define the message and the custom keyword to use for encryption
text = 'Hello Zaira'
custom_key = 'python'

# Vigenère cipher function
def vigenere(message, key):
    key_index = 0  # Keeps track of the position in the key
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Reference alphabet
    encrypted_text = ''  # Stores the encrypted result

    # Loop through each character in the message (converted to lowercase)
    for char in message.lower():
        
        # Keep spaces unchanged in the encrypted message
        if char == ' ':
            encrypted_text += char
        else:
            # Get the corresponding character from the key (wraps around with %)
            key_char = key[key_index % len(key)]
            key_index += 1  # Move to the next key character

            # Calculate how much to shift based on key character's position in alphabet
            offset = alphabet.index(key_char)

            # Find index of current character in alphabet
            index = alphabet.find(char)

            # Apply the shift (Vigenère logic) and wrap around if needed
            new_index = (index + offset) % len(alphabet)

            # Append the encrypted character to the result
            encrypted_text += alphabet[new_index]

    return encrypted_text

# Encrypt the message using the Vigenère cipher
encryption = vigenere(text, custom_key)

# Print the encrypted result
print(encryption)
