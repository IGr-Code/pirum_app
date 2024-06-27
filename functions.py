import os
import string
import exiftool



def caesar():
    
    #Aditional functions
    def is_symbol(char):
        # Define a string containing all symbols
        symbols = string.punctuation  # Includes !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

        # Check if the character is in the symbols string
        return char in symbols
    
    
    
    print('''
          ⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠄⠸⠀⠰⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣿⣿⣶⣶⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢓⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠈⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⢀⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⡿⠃⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⡇⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⡇⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣧⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ''')
    print('''
        CAESAR CIPHER
          ''')
    
    start_decode = True
    
        
    print('''
        q - quit
          ''')    
    
    
    
    while start_decode == True:
        
        
        #Type text to decode
        text = str(input("\n\nText to decode >>> "))
        
        start = True
        
        eng = 26
        encrypted_text = ""
        
        
        global brute_forse
        
        #Check type of decoding
        while start == True:
            print('Type shift number / h - bruteforse mode')
            print('\n q - quit')
            shift = str(input("\n>>> ")).strip()
            
            #BruteForse
            if shift == 'h' or shift == 'H':
                brute_forse = True
                start = False
                
            elif shift == 'q' or shift == 'Q':
                print('Good bye!')
                quit()
                
            #Simple Shift
            elif shift.isdigit():
                shift = int(shift)
                brute_forse = False
                start = False
                
            #Error preventing
            else:
                print('Error! missing number')
                start = True
                
                
        # Start simple Shift mode
        if brute_forse == False:

            
            for char in text:
        
                if char.isalpha():  # Check if character is alphabetic
                    
                    if char.islower():  # Check if character is lowercase
                        new_char = chr((ord(char) - ord('a') - shift) % eng + ord('a'))
                    else:  # Character is uppercase
                        new_char = chr((ord(char) - ord('A') - shift) % eng + ord('A'))
        
                else:  # Character is a symbol or whitespace or digit
                    new_char = char
        
                encrypted_text += new_char
                
            print('\nDescripted text:\n')
            print(encrypted_text)
                
        # Start BruteForse mode        
        elif brute_forse == True:
            
            result = ''
            
            for shift in range(eng):
                
                encrypted_text = ""  # Initialize encrypted text for each shift
                
                
                
                
                for char in text:
        
                    if char.isalpha():  # Check if character is alphabetic
                    
                        if char.islower():  # Check if character is lowercase
                            new_char = chr((ord(char) - ord('a') - shift) % eng + ord('a'))
                        else:  # Character is uppercase
                           new_char = chr((ord(char) - ord('A') - shift) % eng + ord('A'))
        
                    else:  # Character is a symbol or whitespace or digit
                        new_char = char

                    
                    encrypted_text += new_char

                result = result + f'\n[Shift {eng - shift}] {encrypted_text}'
                print(f'\n[Shift {shift}] {encrypted_text}')
                
                
            # Save result option prompt
            print('\n ---------SAVE?----------- ')
            print("\nTo save results, type a file path (e.g., example_name.txt) or type 'n' to not save:")

            # Get file path from user input
            file_path = input('>>> ')

            # Check if the user opted not to save
            if file_path.lower() == 'n':
                print("Results not saved.")
            else:
                try:
                    # Attempt to save or append to the specified file
                    if not os.path.exists(file_path):
                        # If the file doesn't exist, create it
                        with open(file_path, 'w') as file:
                            file.write(result)
                            print(f"File '{file_path}' created and text saved.")
                    else:
                        # If the file exists, append to it
                        with open(file_path, 'a') as file:
                            file.write("\n" + result)  # Append text to existing file
                            print(f"Text appended to '{file_path}'.")

                except Exception as e:
                    # Handle any exceptions that occur during file operation
                    print(f"Error saving results to '{file_path}': {str(e)}")
            
            
            
            
             
        #Close programme
        
        escape = str(input("\nContinue? [y/n] > "))
        
        if escape == 'y' or escape == 'Y':
            start_decode = True
        else:
            start_decode = False
            quit()
    
    
    
from exiftool import ExifToolHelper
   
def meta_data():
    with ExifToolHelper() as et:
        for d in et.get_metadata("DSCN0010.jpg"):
            for k, v in d.items():
                print(f"Dict: {k} = {v}") 
    



