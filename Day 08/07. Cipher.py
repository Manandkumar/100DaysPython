#define Alphabets
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
#define functions
def cipher (plain_text,shift_amount,option):
    cipher_text=""
    
    for letter in plain_text:
        position = alphabet.index(letter)
        if (option =='e'):
            new_position = position +shift_amount
        elif (option =='d'):
            new_position = position -shift_amount
        new_letter = alphabet[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")

# User Inputs 
action = input("Type 'E' for Encode or 'D' for decode: ").lower()
u_text =input ("Type your message: ").lower()
u_shift = int(input("Type the shift number:"))

cipher(plain_text=u_text,shift_amount=u_shift, option=action)
