import sys

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def format_output(encoded_text):
    formatted = ""
    counter = 0
    for char in encoded_text:
        if char.isalpha():
            if counter == 5:
                formatted += " "
                counter = 0
            formatted += char
            counter += 1
    return formatted.upper()

if len(sys.argv) != 2:
    print("Usage: python3 mycipher.py <shift>")
    sys.exit(1)

shift = int(sys.argv[1]) % 26
message = input("Enter the message to encode: ")
message = message.upper().replace(" ", "")
encoded_message = caesar_cipher(message, shift)
formatted_message = format_output(encoded_message)
print(formatted_message)