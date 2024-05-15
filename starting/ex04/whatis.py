import sys

if (len(sys.argv) == 1):
    sys.exit()
elif (len(sys.argv) > 2):
    print('AssertionError: more than one argument are provided')
    sys.exit()
elif (not sys.argv[1].lstrip('-').isdigit()):
    print('AssertionError: argument is not an integer')
    sys.exit()

if (int(sys.argv[1]) % 2 != 0):
    print("I'm Odd.")
else:
    print("I'm Even.")
