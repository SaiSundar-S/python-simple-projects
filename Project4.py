alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    cipher_key=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_key+=alphabet[new_position]
        else:
            cipher_key+=char
    print("after encryption",cipher_key)


def decryption(cipher_key, shift_key):
    plain_text= ""
    for char in cipher_key:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text+=char

    print("after decryption", plain_text)

end_program=False
while not end_program:
    what_to_do=input("type 'encrypt' for encryption, type 'decrypt' for decryption")
    text=input("type your message").lower()
    shift=int(input("enter the shift number"))

    if what_to_do=='encrypt':
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(text,shift_key=shift)
    else:
        print("invalid input")
    play_again=input("type 'yes' to continue,type 'no' to exit \n")
    if play_again=='no':
        end_program=True
        print("nice day")


