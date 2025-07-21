# Original message to encrypt
text = 'Hello Zaira'

# Number of positions to shift each letter
shift = 3

# Define a function to encrypt the message using Caesar cipher
def caesar():
  # All the lowercase letters in the English alphabet
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  # This will store the final encrypted message
  encrypted_text = ''

  # Go through each character in the message (converted to lowercase)
  for char in text.lower():
    # If it's a space, just add it as-is
    if char == ' ':
      encrypted_text += char
    else:
      # Find the position of the character in the alphabet
      index = alphabet.find(char)

      # Shift the index forward by the value of `shift`, wrapping around the alphabet
      new_index = (index + shift) % len(alphabet)

      # Add the new encrypted letter to the final string
      encrypted_text += alphabet[new_index]

  # Print both the original and encrypted message
  print('plain text:', text)
  print('encrypted text:', encrypted_text)

# Call the function to run the Caesar cipher
caesar()


