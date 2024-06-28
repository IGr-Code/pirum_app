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
            file_path = str(input('>>> '))

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
    
    
import base64

def base64_mode():
    
    #DECODE MODE
    def base64_decode(encoded_string):

        decoded_string = ''

        try:
            decoded_bytes = base64.b64decode(encoded_string)
            decoded_string = decoded_bytes.decode('utf-8')  # Assuming UTF-8 encoding
            print("\nDecoded text", decoded_string)
        except Exception as e:
            print(f"\nError decoding Base64: {str(e)}")


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
                        file.write(decoded_string)
                        print(f"File '{file_path}' created and text saved.")
                else:
                    # If the file exists, append to it
                    with open(file_path, 'a') as file:
                        file.write("\n" + decoded_string)  # Append text to existing file
                        print(f"Text appended to '{file_path}'.")

            except Exception as e:
                # Handle any exceptions that occur during file operation
                print(f"Error saving results to '{file_path}': {str(e)}")
 


    #ENCODE mode
    def base64_encode(data):

        if isinstance(data, str):
            # Encode string to bytes using UTF-8 encoding
            data_bytes = data.encode('utf-8')
        elif isinstance(data, bytes):
            data_bytes = data
        else:
            raise TypeError("Input data must be a string or bytes")

        # Perform Base64 encoding
        encoded_bytes = base64.b64encode(data_bytes)

        # Convert bytes back to a UTF-8 encoded string
        encoded_string = encoded_bytes.decode('utf-8')

        print("\nEncoded text", encoded_string)

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
                        file.write(encoded_string)
                        print(f"File '{file_path}' created and text saved.")
                else:
                    # If the file exists, append to it
                    with open(file_path, 'a') as file:
                        file.write("\n" + encoded_string)  # Append text to existing file
                        print(f"Text appended to '{file_path}'.")

            except Exception as e:
                # Handle any exceptions that occur during file operation
                print(f"Error saving results to '{file_path}': {str(e)}")
 

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
    DECODE Base64 | ENCODE Base64
          ''')
   

    start_base64 = True

    while start_base64 == True:

        #Type text to decode
        text = str(input("\nType text >>> "))

        ch_mode = True

        while ch_mode == True:
            print ("[d] - decode\n[e] - encode\n[q] - quit")
            mode = str(input(">>>"))

            #Decode mode
            if mode == 'd' or mode == 'D':
                base64_decode(text)
                ch_mode = False

            #Encode mode
            elif mode == 'e' or mode == 'E':
                base64_encode(text)
                ch_mode = False

            #quit
            elif mode == 'q' or mode == 'Q':
                print("Exiting programme")
                quit()

            #errors
            else:
                print("\nPlease write correct input")
                ch_mode = True

        #Close programme
        
        escape = str(input("\nContinue? [y/n] > "))
        
        if escape == 'y' or escape == 'Y':
            start_base64 = True
        else:
            start_base64 = False
            quit()
 
 
 
 




    
from exiftool import ExifToolHelper
   
def meta_data():

    
         

    def delete_metadata(file_path):
        with ExifToolHelper() as et:
            et.execute(f'-all=', file_path)
            print(f"Deleted metadata for '{file_path}'") 


    start_metadata = True

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
        METADATA GAINING
          ''')

    while start_metadata == True:
    
        file_input = True

        global result_meta
        result_meta = ""
    
        while file_input == True:
            
            

            # Get file path from user input
            print("\nPrint [q] to quit")
            file_path = str(input('Type filepath >>> '))

            #Check if the user opted not to save
            if file_path.lower() == 'q':
                print("Operation stopped")
                quit()
            else:
                try:
                    # Attempt to save or append to the specified file
                   if not os.path.exists(file_path):
                       # If the file doesn't exist, error
                       print(f"ERROR!\nFile '{file_path}' doesn't exist")
                       file_input = True
                       break

                
                  # If the file exists, continue
                   file_input = False

                except Exception as e:
                   # Handle any exceptions that occur during file operation
                   print(f"Error gaining metadata '{file_path}': {str(e)}")
                   file_input = True
            
        ch_mode = True

        while ch_mode == True:
            print ("\nGAIN METADATA | DELETE METADATA")
            print ("[g] - gain metadata\n[d] - delete metadata\n[q] - quit")
            mode = str(input(">>>"))


            #Gaininf info mode
            if (mode == 'g') or (mode == 'G'):

                # Assuming ExifToolHelper is correctly defined elsewhere
                with ExifToolHelper() as et:
                    try:
                        for d in et.get_metadata(file_path):
                            for k, v in d.items():
                                result_meta = result_meta + f"\nDict: {k} = {v}" 
                                print(f"Dict: {k} = {v}")
                    except Exception as e:
                        print(f"Error getting metadata for '{file_path}': {str(e)}") 

    
        
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
                                file.write(result_meta)
                                print(f"File '{file_path}' created and text saved.")
                        else:
                            # If the file exists, append to it
                            with open(file_path, 'a') as file:
                                file.write("\n" + result_meta)  # Append text to existing file
                                print(f"Text appended to '{file_path}'.")

                    except Exception as e:
                        # Handle any exceptions that occur during file operation
                        print(f"Error saving results to '{file_path}': {str(e)}")

                ch_mode = False
 
            elif mode == 'd' or mode == 'D':
                delete_metadata(file_path)

                ch_mode = False
            
            elif mode == 'q' or mode == 'Q':

                print("\nExiting programme")
                ch_mode = False
                quit()

            else:
                print("\nPlease write correct input")
                ch_mode = True
                

     


        #Close programme
        
        escape = str(input("\nContinue? [y/n] > "))
        
        if escape == 'y' or escape == 'Y':
            start_metadata = True
        else:
            start_metadata = False
            quit()
 


