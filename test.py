
import sys

print( 'Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
if len(sys.argv)>1:
    print('hello')
    print(sys.argv[1])