
# Example 01
avengers = {'old':'steve','rich':'tony','god':'thor'} # remove the closing bracket to see the error
print(avengers)

# Example 02
print('List:',[x for x in range(10)]) # remove the closing square bracket to see the error

# Example 03
print({(x,y) for x,y in zip('abcd','1234')}) # remove the square bracket from x,y to see the error

# Example 04
avengers = {
            'old':'steve',
            'rich':'tony' # remove this value to see the error
            }
print(avengers)

# Example 05
try:
    print('Hello Python')
except (ValueError, AttributeError): # remove these brackets to see the error
    print('Problem Happened')

# Example 06
try:
    print('Hello Python')
except: # Remove this except keyword, indent the below statement outside the try block and see the error
    print('Only Try Block is Present')

# Example 07
num = 5
if num > 1: # remove the colon to see the error
    print('True')

# Example 08
num = 5
if num == 1: # replace the == with = to see the error
    print('True')
else:
    print('False')

# Example 09
old_avengers = ['steve','tony','thor','hulk','natasha','hawkeye']
new_avengers = ['antman','peter','stephen','Tchala','wong']
avengers = [*old_avengers, *new_avengers]
print(avengers)
print(f'The Original Avengers are {old_avengers}') # put * with old_avengers to see the error

# Example 10
num = 1
if num > 5:
    print('True') # unindent this line to see the error
else:
    print('False') # unindent this line to see the error

# Example 11
import collections
collections.namedtuple # misspell this word namedtuple to see the error
num = 3
print(num) # misspell this word namedtuple to see the error