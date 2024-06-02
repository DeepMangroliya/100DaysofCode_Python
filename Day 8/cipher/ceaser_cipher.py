from art import logo # type: ignore

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print (logo)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# again = 'Y'

def ceaser(again):
    while again=='Y':
        end_text = ""
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        for letter in text:

            if letter in alphabet:
                position = alphabet.index(letter)

                if direction == "encode":
                    new_position = (position + shift) % len(alphabet) 

                else:
                    new_position= (position - shift) % len(alphabet)
                
                end_text+=alphabet[new_position]
            else:
                end_text+=letter

        if len(end_text) != 0:
            print(f"The {direction}d code is {end_text}")
        
        again = input("Play Again? 'Y' for Yes 'N' for No.")

ceaser(again='Y') 