# text-to-morse
This code is a Python program that converts a given text string into Morse code. It uses a dictionary named 'morse_code' that maps each letter, number, and special character to its corresponding Morse code symbol. The program accepts user input using the 'input()' function and then uses a 'while' loop to keep accepting input until the user types "exit".

Inside the loop, the program uses the 'upper()' method to convert the input string to uppercase (since the Morse code symbols are all uppercase). It then uses a list comprehension to create a list of Morse code symbols by looking up each character in the 'morse_code' dictionary using the 'get()' method. If the character is not found in the dictionary (i.e., it's not in the keys), the 'get()' method returns an empty string.

Finally, the program uses the 'join()' method to join the Morse code symbols into a single string, separated by spaces. If the resulting Morse string is empty, the program prints a message indicating that no Morse code was found for the given input. Otherwise, it prints the Morse string.

Note that this code also includes additional characters in the 'morse_code' dictionary compared to the original code. These characters include '!', '&', ',' '(', ')', '+', '-', '/', ':', ';', '=',' _', '%', and '@'.
