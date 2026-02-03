MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(text):
    text = text.upper()
    morse_text = ''
    for letter in text:
        if letter == ' ':
            morse_text += '   '
        else:
            code = MORSE_CODE_DICT.get(letter, '')
            if code:
                morse_text += code + ' '
    return morse_text.strip()


counting=True
while counting:
    text=input('Enter your text or press exit to Q: ')
    if(text.upper()=="Q"):
        counting=False
        break
    print(f"Morse Code: {encrypt(text)}")


