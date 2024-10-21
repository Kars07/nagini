import string
def decrypt(encrypted_code, key_value):
    key_code = string.ascii_uppercase
    decrypt_positon = []
    decrypt_plain_text = []
    
    for char in encrypted_code:
        keycode_position = key_code.index(char.upper())
        
        new_keycode_position = keycode_position - key_value

        if new_keycode_position < 0:
            new_keycode_position += 26
            
        decrypt_positon.append(new_keycode_position)
        decrypt_plain_text.append(key_code[new_keycode_position])
    
    return decrypt_positon, decrypt_plain_text

encrypted_code = input("INPUT ENCRYPTED CODE: ").upper()
if all(char in string.ascii_uppercase for char in encrypted_code):
    key_value = int(input("Input Key value:"))
    
    decrypted_position, decrypted_plain_text = decrypt(encrypted_code, key_value)
    print(f"Encrypted Code: {encrypted_code}")
    print(f"Decrypted Position: {decrypted_position}")
    print(f"Decrypted to Plain text: {decrypted_plain_text}")
else:
    print("Invalid Encrypted Code")    
    