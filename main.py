import winsound
import time



unit = 100   
frequency = 480 


morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',  
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',  
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',  
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',  
    'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',  
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    '.': '.-.-.-',  ',': '--..--',  '?': '..--..',  "'": '.----.', 
    '!': '-.-.--',  '/': '-..-.',   '(': '-.--.',   ')': '-.--.-', 
    '&': '.-...',   ':': '---...',  ';': '-.-.-.',  '=': '-...-', 
    '+': '.-.-.',   '-': '-....-',  '_': '..--.-',  '"': '.-..-.', 
    '$': '...-..-', '@': '.--.-.',
}


def dot():
    winsound.Beep(frequency, 1 * unit)

def dash():
    winsound.Beep(frequency, 3 * unit)

def space():
    time.sleep(1)

def translate_text():
    user_input = input('What would you like to translate from English to Morse code? \n')
    user_input = user_input.upper()
    morse_code = []
    if not user_input:
        print('Please enter some text')
        
    

    for char in user_input:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        elif char == ' ':
            morse_code.append(' ')  
    print(morse_code)
    return morse_code


def audio(morse_code):
    for symbol in morse_code:
        if symbol == ' ':
            time.sleep(7 * unit / 1000)  
        
        else:
            for char in symbol:  
                if char == '.':
                    dot()
                elif char == '-':
                    dash()
                time.sleep(1 * unit / 1000)  
            time.sleep(3 * unit / 1000)  


on_switch = True

while on_switch == True:
    translation = translate_text()
    audio(translation)
    wants_to_continue = input('Would you like to translate another? Y/N')
    wants_to_continue = wants_to_continue.upper()
    if wants_to_continue == 'N':
        on_switch = False
    

