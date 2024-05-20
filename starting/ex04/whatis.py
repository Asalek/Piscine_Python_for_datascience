import sys

if (len(sys.argv) == 1):
    sys.exit()
elif (len(sys.argv) > 2):
    print('AssertionError: more than one argument are provided')
    sys.exit()
try:
    a = int(sys.argv[1], base=10)
except:
    a = None

if a is None:
    print('AssertionError: argument is not an integer')
    sys.exit()

print("I'm Odd." if a % 2 != 0 else "I'm Even.")
