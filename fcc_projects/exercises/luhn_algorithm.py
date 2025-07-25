# Function to verify the card number using the Luhn Algorithm
def verify_card_number(card_number):
    sum_of_odd_digits = 0  # Initialize sum for digits at odd positions (from the right)
    
    # Reverse the card number for easier indexing (Luhn processes from right to left)
    card_number_reversed = card_number[::-1]

    # Get all digits at odd positions (indexes 0, 2, 4, ...) after reversal
    odd_digits = card_number_reversed[::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)  # Directly add these digits to the sum

    sum_of_even_digits = 0  # Initialize sum for processed even-position digits

    # Get all digits at even positions (indexes 1, 3, 5, ...) after reversal
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2  # Double the digit
        if number >= 10:
            # If the result is two digits, add the digits together (e.g., 12 → 1 + 2 = 3)
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number  # Add to total even-position sum

    # Total sum of processed odd and even digits
    total = sum_of_odd_digits + sum_of_even_digits

    # Return True if total modulo 10 is zero (valid card), else False
    return total % 10 == 0

# Main function to run the verification
def main():
    card_number = '4111-1111-4555-1142'  # Example card number (with dashes)
    
    # Remove dashes and spaces to clean the input
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Call the verification function
    if verify_card_number(translated_card_number):
        print('VALID!')  # Card passes the Luhn check
    else:
        print('INVALID!')  # Card fails the Luhn check

# Call the main function
main()
