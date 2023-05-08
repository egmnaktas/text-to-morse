# text-to-morse
This Python code allows the user to input a string of characters and converts it to its equivalent Morse code symbols. 
Here's how the code works:

The code defines a dictionary called morse_code that maps each character to its Morse code symbol.

The code prompts the user to input the text they want to be converted, which is stored in the user_text variable.

The code uses a list comprehension to create a list of Morse code symbols. For each character in the user_text string, the code checks if the character exists in the morse_code dictionary. If it does, the corresponding Morse code symbol is added to the list. If the character does not exist in the dictionary, an empty string is added to the list.

The list of Morse code symbols is joined into a string using the str.join() method with a space character as the separator. The resulting string is stored in the morse_string variable.

The code checks if the morse_string variable is empty. If it is, it means that none of the characters in the user_text string had a corresponding Morse code symbol in the morse_code dictionary. The code prints a message to inform the user of this. If the morse_string variable is not empty, the code prints the resulting Morse code string.

Note that this code also includes additional characters in the morse_code dictionary compared to the original code. These characters include !, &, ', (, ), +, -, /, :, ;, =, _, %, and @.
