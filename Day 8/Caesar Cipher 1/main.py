alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text,shift_amount):
    ori_tex = ""
    for tet in original_text:
        if tet in alphabet:
            num=alphabet.index(tet)+shift_amount
            ori_tex+=alphabet[num]
        else:
            ori_tex+=tet
    print(ori_tex)
def decrypt(decry,shift_number):
    ori_tex= ""
    for tex in decry:
        if tex in alphabet:
            num = alphabet.index(tex)-shift_number
            ori_tex += alphabet[num]
        else:
            ori_tex += tex
    print(ori_tex)

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
if direction=="encode":
    encrypt(text,shift)
valid=input("do you want to decrypt??")

if valid=="yes":
    dec=input("Type the encrypt value: ")
    shift_num=int(input("type the original shift number: "))
    decrypt(dec,shift_num)

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

