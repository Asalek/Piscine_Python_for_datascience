import sys


def text_analyzer(Givenstring=""):
    '''This function counts the number of upper characters,
    lower characters, punctuation and spaces in a given text.'''
    text = Givenstring
    punctuations = "=!\"[\\]+#@%$,-./:;<>?&'()*+`}~{|^_"

    if (text == ""):
        print("No Text Given")
        return
    total = len(text)
    # increment with one if the condition is true
    upper = sum(1 for c in text if c.isupper())
    puncm = sum(1 for c in text if c in punctuations)
    space = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())
    lower = sum(1 for c in text if c.islower())
    print(
        "The text contains ", total, " character(s):\n",
        upper, " upper letter(s)\n",
        lower, " lower letter(s)\n",
        puncm, " punctuation mark(s)\n",
        space, " space(s)\n",
        digits, " digit(s)"
    )


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("What is the text to count?")
        try:
            text = input(">>>")
            text_analyzer(text)
        except TypeError:
            pass
        except KeyboardInterrupt:
            print("\n\tSee Ya (^_^)")
            exit()
        except EOFError:
            print("\n\tSee Ya (^_^)")
            exit()
    elif (not isinstance(sys.argv[1], str)):
        print("AssertionError: argument is not a string")
    else:
        text_analyzer(sys.argv[1])

# def main():
#     print("This is the main function")
# if __name__ == "__main__":
# 	main()

# don't forget to add - when cp frm pdf tst or u get 1 miss penct
