letter_to_morse = {
    "A": "·−", "B": "−···", "C": "−·−·", "D": "−··", "E": "·", "F": "··−·", "G": "−−·", "H": "····", "I": "··", "J": "·−−−", "K": "−·−", "L": "·−··", "M": "−−", "N": "−·", "O": "−−−", "P": "·−−·", "Q": "−−·−", "R": "·−·", "S": "···", "T": "−", "U": "··−", "V": "···−", "W": "·−−", "X": "−··−", "Y": "−·−−", "Z": "−−··",
    "1": "·−−−−", "2": "··−−−", "3": "···−−", "4": "····−", "5": "·····", "6": "−····", "7": "−−···", "8": "−−−··", "9": "−−−−·", "0": "−−−−−",
    "À, Å": "·−−·−", "Ä": "·−·−", "È"	: "·−··−", "É"	: "··−··", "Ö": "−−−·", "Ü"	: "··−−", "ß": "···−−··", "CH": "−−−−", "Ñ"	: "−−·−−", ".": "·−·−·−", ",": "−−··−−", ":": "−−−···", ";": "−·−·−·", "?": "··−−··", "-": "−····−", "_": "··−−·−", "(": "−·−−·", ")"	: "−·−−·−", "'": "·−−−−·", "=": "−···−", "+": "·−·−·", "/": "−··−·", "@": "·−−·−·"
}

# −− −−− ·−· ··· ·  −·−· −−− −·· ·
# ··· ··− ···· ·− −·−− −···
# ··· ··− ···· ·− −·−− −···   ··· ·− −· ·−


def clean_morse(user_input: str) -> list:
    list_input = user_input.replace('\t', '  ').split(" ")
    return list_input


def clean_text(user_input: str) -> list:
    return list(user_input.upper())


def translate(user_input):
    translated = []
    if "·" in user_input or "−" in user_input:
        list_input = clean_morse(user_input)
        morse_to_letter = {v: k for k, v in letter_to_morse.items()}
        for char in list_input:
            if char == '':
                translated.append(' ')
            elif letter := morse_to_letter.get(char):
                translated.append(letter)

        sentence = ''.join(translated)

    else:
        list_input = clean_text(user_input)
        for char in list_input:
            if char == ' ':
                translated.append('')
            elif morse := letter_to_morse.get(char):
                translated.append(morse)

        sentence = ' '.join(translated)

    return sentence


print("Welcome to Morse Code Translator")
print("You may translate from Morse to text or from text to Morse")
print(". = •")
print("-- = ▬")
print("space = tab")
user_input = input("Please enter the code: ")
print(translate(user_input))
