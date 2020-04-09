# Filename: project_1.py
### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME:
# STUDENT ID:
# SECTION:
############      DEFINE CONSTANTS BELOW      ############


############       ADD YOUR CODE BELOW        ############
def convert_decimal_to_base(decimal_number, base):
    remainder_track = ''
    decimal_number = int(decimal_number)
    if decimal_number == 0 or base == 10:
        return str(decimal_number)
    while decimal_number > 0:
        remaindern = decimal_number % base
        remainder = dec_to_hexdigit(remaindern)
        remainder_track = str(remainder) + remainder_track
        decimal_number = decimal_number // base
    return remainder_track


# ******* IMPORTANT YOU NEED TO uncomment the following line and complete the body of the function
def dec_to_hexdigit(decdig):
    # Returns the propper hexadecimal digit (letter) in cases from 10-15 (Decimal).
    if decdig == 10:
        return "A"
    elif decdig == 11:
        return "B"
    elif decdig == 12:
        return "C"
    elif decdig == 13:
        return "D"
    elif decdig == 14:
        return "E"
    elif decdig == 15:
        return "F"
    else:
        return str(decdig)


# ******* IMPORTANT YOU NEED TO uncomment the following line and complete the body of the function
def hex_to_decdigit(hexdigit):
    # This will accept either UPPERCASE or lowercase hexadecimal digits.
    if hexdigit == "A" or hexdigit == "a":
        return '10'
    elif hexdigit == "B" or hexdigit == "b":
        return '11'
    elif hexdigit == "C" or hexdigit == "c":
        return '12'
    elif hexdigit == "D" or hexdigit == "d":
        return '13'
    elif hexdigit == "E" or hexdigit == "e":
        return '14'
    elif hexdigit == "F" or hexdigit == "f":
        return '15'
    else:
        return str(hexdigit)

        # ******* IMPORTANT YOU NEED TO uncomment the following line and complete the body of the function. hint: use a loop to iterate trough the string numberb


# Needs to be redefine to be independent!
def convert_base_to_decimal(numberb, base):
    # Initialization of variables to prevent bugs
    power = 1
    num = 0
    for i in range(len(numberb) - 1, -1, -1):
        # Input (numberb) must be less than the number of the base
        if val_of_char(numberb[i]) >= base:
            print('Invalid Number')
            return -1
        num += val_of_char(numberb[i]) * power
        power = power * base
    return num


# ###################################################### #
# The purpose of this function is to implement it in the convert_base_to_decimal()
# Returns the value of a char for Hexadecimal purposes.
def val_of_char(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10
# ###################################################### #

# *******IMPORTANT YOU NEED TO uncomment the following line and complete the body of the function
def convert_base1_to_base2(b1num, b1, b2):
    dec_b1num = convert_base_to_decimal(b1num, b1)
    new_b1num = convert_decimal_to_base(dec_b1num, b2)
    return new_b1num


def process_conversion(numericOption):  # This function will process the valid  selections
    # First option
    if numericOption == 1:
        dec_num = int(input("Enter the number to be converted: "))
        base = int(input('Enter the output base: '))
        if base == 2 or base == 8 or base == 16:
            bnumber = convert_decimal_to_base(dec_num, base)
            print("The decimal number " + str(dec_num) + ' is ' + bnumber + ' in base ' + str(base))
        else:
            base = int(input("Invalid base!\nEnter the correct output base (2, 8 or 16): "))
            bnumber = convert_decimal_to_base(dec_num, base)
            print("The decimal number " + str(dec_num) + ' is ' + bnumber + ' in base ' + str(base))
    # Second Option
    elif numericOption == 2:
        bnum_dec = input("Enter the number you want to convert: ")
        base = int(input("Enter the base of the number (2, 8 or 16): "))
        # Validates the base so that it's Binary, Octal or Hexadecimal
        if base == 2:
            new_num2 = convert_base_to_decimal(bnum_dec, base)
            print("The number " + bnum_dec + " in base " + str(base) + " is " + str(new_num2) + " in decimal.")
        elif base == 8:
            new_num8 = convert_base_to_decimal(bnum_dec, base)
            print("The number " + bnum_dec + " in base " + str(base) + " is " + str(new_num8) + " in decimal.")
        elif base == 16:
            new_num16 = convert_base_to_decimal(bnum_dec, base)
            print("The number " + bnum_dec + " in base " + str(base) + " is " + str(new_num16) + " in decimal.")
    elif numericOption == 3:
        b1num = input("Enter the number you want to convert: ")
        base1 = int(input("Enter the base of the number: "))
        base2 = int(input("Enter the base you want to convert to: "))
        new_btb_num = convert_base1_to_base2(b1num, base1, base2)
        print("The number " + b1num + " in base " + str(base1) + " is " + str(new_btb_num) + " in " + str(base2) + ".")

    ####*********IMPORTAN Add code to handle other menu selections.


# This function needs to be called inside the main() function
def print_program_menu():
    print("\n--------")
    print("Welcome to the base conversion program. Please, choose an option:")
    print("1. Decimal to Binary, Octal or Hexadecimal")
    print("2. Binary, Octal or Hexadecimal to Decimal")
    print("3. Binary, Octal or Hexadecimal to Binary, Octal or Hexadecimal")
    print("4. Exit")


# This function verify if the entered option is an integer
def identify_option(option):
    # Verify that a number was input and it is in valide renge
    try:
        numericOption = int(option)
        return numericOption
    except:
        return -1  # invalid option


# *******NEED TO uncomment the following line and complete the body of the function**********
def main():
    not_done = True
    while not_done:
        print_program_menu()
        user_option = input("Please, enter your option: ")
        option_info = identify_option(user_option)
        if option_info != -1 and (1 <= int(user_option) <= 4):
            user_option = int(user_option)
            if user_option == 4:
                not_done = False
                print("Thank you for using the base conversion program.")
            else:
                process_conversion(user_option)
        else:
            print("Invalid option.\n")


##*******NEED TO uncomment the following line. The line makes python start the program from the main function


if __name__ == "__main__":
    main()
