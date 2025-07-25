
# Original message to encrypt
text = 'Hello Zaira'

# Number of positions to shift each letter
shift = 3


def caesar(message, offset):
    # Define the alphabet used for the cipher
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Initialize the encrypted text variable
    encrypted_text = ''

    # Loop through each character in the input message
    for char in message.lower():
        # Preserve spaces without encryption
        if char == ' ':
            encrypted_text += char
        else:
            # Find the index of the character in the alphabet
            index = alphabet.find(char)
            # Compute the new index by adding the offset and wrapping around using modulo
            new_index = (index + offset) % len(alphabet)
            # Append the corresponding encrypted character
            encrypted_text += alphabet[new_index]

    # Display original and encrypted text
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Assign values to the variables used in function call
text = message     # Assign the original message to a new variable 'text'
shift = offset     # Assign the original offset to a new variable 'shift'

# Call the function using new variable names
caesar(text, shift)  # Encrypts the message using the specified shift value

# Call the function again using a fixed Caesar shift of 13 (ROT13 encryption)
caesar(text, 13)  # ROT13 is a common Caesar cipher variation that rotates by 13 positions


