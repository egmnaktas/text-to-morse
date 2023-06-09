morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/', ',': '--..--', '?': '..--..', '.': '.-.-.-', '$': '...-..-', '!': '-.-.--', '&': '.-...',
    '\'': '.----.', '(': '-.--.', ')': '-.--.-', '+': '.-.-.', '-': '-....-', '/': '-..-.', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '_': '..--.-', '@': '.--.-.', '%': '-..-.'
}
while True:
    user_text = input('Type the text you want to be converted (type "exit" to quit): ').upper()
    if user_text == "EXIT":
        break
    morse_code = [morse_code.get(char, '') for char in user_text]
    morse_string = ' '.join(morse_code)
    if not morse_string:
        print('No morse code found for the given input')
    else:
        print(morse_string)
