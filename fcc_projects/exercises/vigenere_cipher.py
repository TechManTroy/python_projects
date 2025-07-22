# Original text to encrypt
text = 'Hello Zaira'

# Instead of using a fixed number shift like Caesar, we use a word as the key
custom_key = 'python'

# Function name changed from 'caesar' to 'vigenere'
def vigenere(message, key):
    '''
    The key is usually shorter than the message.
    We use key_index to keep track of where we are in the key,
    and use it in a loop so the key repeats as needed.
    '''
    key_index = 0  # Start at the first letter of the key
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''  # To store the final result

    # Go through each character in the message
    for char in message.lower():
        # If it's a space, just add it to the encrypted text
        if char == ' ':
            encrypted_text += char
        else:
            # Get the letter from the key (repeat using % if needed)
            key_char = key[key_index % len(key)]

            # Move to the next letter in the key
            key_index += 1

            # Get shift amount based on the key character's position in the alphabet
            offset = alphabet.find(key_char)

            # Get position of the current message character in the alphabet
            index = alphabet.find(char)

            # Add the shift and wrap around if needed
            new_index = (index + offset) % len(alphabet)

            # Add the encoded character to the encrypted result
            encrypted_text += alphabet[new_index]

    # Print original and encrypted text
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Call the function using your text and custom key
vigenere(text, custom_key)
