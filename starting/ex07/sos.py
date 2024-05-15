import sys


def main():
    code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }

    if len(sys.argv) != 2:
        print("Usage: python sos.py <message>")
        return
    lenght = (i for i in sys.argv[1].upper() if i in code)
    lenght2 = len(sys.argv[1])
    if (len(list(lenght)) != lenght2):
        print("AssertionError: the arguments are bad")
        return
    print(" ".join([code[c] for c in sys.argv[1].upper() if c in code]))


main()
