from random import randint
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def generate_otp(sheets, length):    
    for sheet in range(sheets):
        with open("otp" + str(sheet) + ".txt", "w") as f:
            for i in range (length):
                f.write(str(randint(0,26))+ "\n")
                
def load_sheet(filename):   
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents

def get_plain_text():   
    plain_text = input("Please type your message: ")
    return plain_text

def load_file(filename):    
    with open(filename, "r") as f:
        contents = f.read()
    return contents

def save_file(filename, data):    
    with open(filename, "w") as f:
        f.write(data)

def encrypt(plaintext, sheet):   
    ciphertext = ''
    for position, character in enumerate(plaintext):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) + int(sheet[position])) %26
            ciphertext += ALPHABET[encrypted]
    return ciphertext

def decrypt(ciphertext, sheet): 
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) %26
            plaintext += ALPHABET[decrypted]
    return plaintext

def menu():
    choices = [1, 2, 3, 4]
    choice = 0
    while True:
        while choice not in choices:
            print('what would you like to do?')
            print('1. Generate one-time pads')
            print('2. Encrypt a mesage')
            print('3. Decrypt a message')
            print('4. Quit the program')
            choice = int(input('Please type 1, 2, 3, or 4, and press Enter: '))

            if choice == 1:
                sheets = int(input('How many different sheets do u want to create? '))
                length = int(input('What is the maximum message length for a message? '))
                generate_otp(sheets, length)

            elif choice == 2:                
                filename = input('What is the name of sheet that you would like to use? ')
                sheet = load_sheet(filename)                
                plaintext = get_plain_text()
                ciphertext = encrypt(plaintext, sheet)
                filename = input('What would you like the name of your encrypted file to be? ')
                save_file(filename, ciphertext)

            elif choice == 3:
                filename = input('What is the name of sheet that you would like to use? ')
                
                sheet = load_sheet(filename)
                filename = input('What is the name of the file that you would like to decrypt? ')
                ciphertext = load_file(filename)
                plaintext = decrypt(ciphertext, sheet)
                print('The message reads: ')
                print("\n\t" + plaintext+ "\n")      
                
            elif choice == 4:
                exit()
            choice = 0

menu()

                                   
                               
