from playsound import playsound
#playsound 1.2.2 version is required
import time
morse_code ={'A':'.-', 'B':'-...', 'C': '-.-.', 'D': '-..',
                'E' : '.', 'F':'..-.', 'G':'--.','H':'....','I':'..',
                'J':'.---','K':"-.-", 'L':".-..", 'M':'--', "N":'-.',
                'O' : '---','P': '.--.', 'Q':'--.-','R':'.-.','S':'...',
                'T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
                '1': '.----', '2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',
                '8':'---..','9':'----.','0':'-----',' ':'/'}

message = input()

message = " ".join(morse_code[c] for c in message.upper())

def play_morse(message):
    for c in message:
        if c == '.':
            playsound('dit.mp3')
            #time.sleep(0.1)
        elif c == '-':
            playsound('dah.mp3')
            #time.sleep(0.001)
        elif c=='/' or c==' ':
            time.sleep(1)
        else:
            print("invalid")
print(message)
play_morse(message)




