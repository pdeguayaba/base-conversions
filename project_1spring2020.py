# Filename: project_1.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME:
# STUDENT ID:
# SECTION:
############      DEFINE CONSTANTS BELOW      ############



############       ADD YOUR CODE BELOW        ############
def convert_decimal_to_base(decimal_number, base):
    remainder_track = ''
    decimal_number=int(decimal_number)
    if decimal_number==0 or base==10:
        return str(decimal_number)
    while decimal_number > 0:
        remaindern = decimal_number % base
        remainder=dec_to_hexdigit(remaindern)
        remainder_track=  str(remainder)+remainder_track
        decimal_number = decimal_number // base
        
    return remainder_track


#******* IMPORTANT YOU NEED TO uncomment the following line and complete the body of the function
def dec_to_hexdigit(decdig):
	bnumber = hex(decdig)
	return bnumber


#******* IMPORTANT YOU NEED TO uncomment the following line and complete the body of the function    
#def hex_to_decdigit(hexdigit):


#******* IMPORTANT YOU NEED TO uncomment the following line and complete the body of the function. hint: use a loop to iterate trough the string numberb
#def convert_base_to_decimal(numberb,base):


#*******IMPORTANT YOU NEED TO uncomment the following line and complete the body of the function        
#def convert_base1_to_base2(b1num,b1,b2):


def process_conversion(numericOption): # This function will process the valid  selections
    if numericOption == 1:
        dec_num=int(input("Enter the number to be converted: "))
        base=int(input('Enter the output base: '))
                        
        bnumber=convert_decimal_to_base(dec_num,base)
        print("The decimal number "+ str(dec_num)+ ' is ' + bnumber + ' in base '+str(base))
      
        
####*********IMPORTAN Add code to handle other menu selections.


# This function needs to be called inside the main() function
def print_program_menu():
    print("\n--------")
    print( "Welcome to the base conversion program. Please, choose an option:")
    print("1. Decimal to Binary, Octal or Hexadecimal")
    print("2. Binary, Octal or Hexadecimal to Decimal")
    print("3. Binary, Octal or Hexadecimal to Binary, Octal or Hexadecimal")
    print("4. Exit")


#This function verify if the entered option is an integer
def identify_option(option):
    # Verify that a number was input and it is in valide renge
    try:
        numericOption=int(option)
        return numericOption
    except:
        return -1 #invalid option


#*******NEED TO uncomment the following line and complete the body of the function**********
def main():
  print_program_menu()
  option = input("Option: ")
  identify_option(option)
  process_conversion(option)




##*******NEED TO uncomment the following line. The line makes python start the program from the main function


if __name__ == "__main__":
    main()
