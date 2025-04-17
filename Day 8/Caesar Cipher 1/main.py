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


if direction=="encode":
    encrypt(text,shift)
valid=input("do you want to decrypt??")

if valid=="yes":
    dec=input("Type the encrypt value: ")
    shift_num=int(input("type the original shift number: "))
    decrypt(dec,shift_num)


