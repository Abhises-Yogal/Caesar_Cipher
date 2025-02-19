""" importing string """
import string

def welcome():
    """ printing welcome message """
    print("Welcome to the Caesar Cipher.")
    print("This program encrypts and decrypts text with the Caesar Cipher.")

def enter_message():
    """ Asks for mode and message to encrypt or decrypt """
    while True:
        mode=input("Would you like to encrypt(e) or decrypt(d)?:")
        if mode in ["e","d"]:
            break
        print("Invalid mode.")
        if mode=="e":
            operation = "encrypt"
        else:
            operation = "decrypt"
    message=input(f"What message would you like to {operation}?:")
    while True:
        try:
            shift=int(input("What is the shift number?:"))
            break
        except ValueError:
            print("Invalid shift")
        message=message.upper()
        return mode,message,shift

def encrypt(message,shift):
    """ code to encrypt message through shift """
    outcome=""
    for char in message:
        if char in string.ascii_uppercase:
            index=(string.ascii_uppercase.index(char)+shift)%26
            outcome+=string.ascii_uppercase[index]
        else:
            outcome+=char
    return outcome

def decrypt(message,shift):
    """ decrypts message through reversing shift """
    return encrypt(message,-shift)

def process_file(filename, mode, shift):
    """ opens file and encrypts or decrypts each line """
    messages=[]
    with open(filename, encoding="utf-8") as f:
        for line in f:
            message=line.strip().upper()
            if mode=="e":
                messages.append(encrypt(message, shift))
            else:
                messages.append(decrypt(message, shift))
    return messages

def is_file(filename):
    """ checks if the file exists or not """
    try:
        with open(filename, encoding="utf-8"):
            return True
    except FileNotFoundError:
        return False

def write_messages(messages):
    """ writes messages to file 'results.txt' """
    with open("results.txt", "w", encoding="utf-8") as f:
        for message in messages:
            f.write(message+"\n")

def message_or_file():
    """ asks user to select the mode """
    while True:
        mode=input("Would you like to encrypt(e) or decrypt(d)?:")
        if mode in ["e","d"]:
            break
        print("Invalid mode")
    while True:
        source=input("Would you like to read from a file(f) or the console(c)?:")
        if source in ["f","c"]:
            break
        print("Invalid source")
    if source=="c":
        message=input("What message would you like to {}?:".format("encrypt" if mode=="e" else "decrypt"))
        message=message.upper()
        return mode, message, None
    else:
        while True:
            filename=input("Enter a filename:")
            if is_file(filename):
                break
            print("Invalid filename")
        return mode, None, filename


def main():
    """ Main function to welcome the user, handle encryption or decryption of messages or 
    files, and loop until the user decides to exit. """
    welcome()
    while True:
        mode, message, filename=message_or_file()
        if filename:
            while True:
                try:
                    shift=int(input("What is the shift number?:"))
                    break
                except ValueError:
                    print("Invalid shift")
            messages=process_file(filename, mode, shift)
            write_messages(messages)
            print("Output written to results.txt")
        else:
            shift=int(input("What is the shift number?:"))
            outcome=encrypt(message,shift) if mode=="e" else decrypt(message,shift)
            print(outcome)
        while True:
            answer=input("Would you like to encrypt or decrypt another message?(y/n):")
            if answer in ["y","n"]:
                break
            print("Invalid input")
        if answer=="n":
            print("Thanks for using the program, goodbye!")
            break

if __name__=="__main__":
    main()
