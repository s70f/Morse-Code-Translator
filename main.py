morse = {
    "A": "·−", "B": "−···", "C": "−·−·", "D": "−··", "E": "·", "F": "··−·", "G": "−−·", "H": "····", "I": "··", "J": "·−−−", "K": "−·−", "L": "·−··", "M": "−−", "N": "−·", "O": "−−−", "P": "·−−·", "Q": "−−·−", "R": "·−·", "S": "···", "T": "−", "U": "··−", "V": "···−", "W": "·−−", "X": "−··−", "Y": "−·−−", "Z": "−−··",
    "1": "·−−−−", "2": "··−−−", "3": "···−−", "4": "····−", "5": "·····", "6": "−····", "7": "−−···", "8": "−−−··", "9": "−−−−·", "0": "−−−−−",
    "À, Å": "·−−·−", "Ä": "·−·−", "È"	: "·−··−", "É"	: "··−··", "Ö": "−−−·", "Ü"	: "··−−", "ß": "···−−··", "CH": "−−−−", "Ñ"	: "−−·−−", ".": "·−·−·−", ",": "−−··−−", ":": "−−−···", ";": "−·−·−·", "?": "··−−··", "-": "−····−", "_": "··−−·−", "(": "−·−−·", ")"	: "−·−−·−", "'": "·−−−−·", "=": "−···−", "+": "·−·−·", "/": "−··−·", "@": "·−−·−·"
}


def clean_data(input_morse):
    clean_morse = input_morse.replace('\t', '  ').split(" ")
    print(input_morse)
    return clean_morse


print("Welcome to Morse Code Translator")
print(". = •")
print("_ = ▬")
print("space = tab")
morse_code = input("Please enter the code:")
