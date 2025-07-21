# Original message to encrypt
text = 'Hello Zaira'

# Number of positions to shift each letter
shift = 3

# Alphabet used for the cipher
 alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Variable to store the encrypted message
 encrypted_text = ''

# Loop through each character in the input text, converted to lowercase
 for char in text.lower():
    
    # If the character is a space, add it to the result as-is
     if char == ' ':
        encrypted_text += char
     else:
        # Find the index of the character in the alphabet string
        index = alphabet.find(char)

        # Calculate the new index by shifting the current index and wrapping around with modulo
        new_index = (index + shift) % len(alphabet)

        # Add the shifted character to the encrypted text
        encrypted_text += alphabet[new_index]

 # Print the final encrypted result
 print('encrypted text:', encrypted_text)

