

def caesar():
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
                        new_char = chr((ord(char) - ord('a') + shift) % eng + ord('a'))
                    else:  # Character is uppercase
                        new_char = chr((ord(char) - ord('A') + shift) % eng + ord('A'))
        
                else:  # Character is a symbol or whitespace or digit
                    new_char = char
        
                encrypted_text += new_char
                
            print('\nDescripted text:\n')
            print(encrypted_text)
                
        # Start BruteForse mode        
        elif brute_forse == True:
            
            for shift in range(eng):
                
                encrypted_text = ""  # Initialize encrypted text for each shift
                
                
                for char in text:
        
                    if char.isalpha():  # Check if character is alphabetic
                    
                        if char.islower():  # Check if character is lowercase
                            new_char = chr((ord(char) - ord('a') + shift) % eng + ord('a'))
                        else:  # Character is uppercase
                           new_char = chr((ord(char) - ord('A') + shift) % eng + ord('A'))
        
                    else:  # Character is a symbol or whitespace or digit
                        new_char = char

                    
                    encrypted_text += new_char
            
                print(f'\n[Shift {eng - shift}] {encrypted_text}')
            
             
        #Close programme
        
        escape = str(input("\nContinue? [y/n] > "))
        
        if escape == 'y' or escape == 'Y':
            start_decode = True
        else:
            start_decode = False
            quit()
    
    
    
    



