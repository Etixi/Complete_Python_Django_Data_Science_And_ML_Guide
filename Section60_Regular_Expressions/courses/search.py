# need to load the re module before use
import re

sentence = 'This is a sample string'
# check if 'sentence' contains the pattern described by RE argument
print(bool(re.search(r'is', sentence)))

# ignore case while searching for a match
print(bool(re.search(r'this', sentence, flags=re.I)))


# example when pattern isn't found in the input string
print(bool(re.search(r'xyz', sentence)))


# re.search output can be directly used in conditional expressions
if re.search(r'ring', sentence):
    print('mission success')

# use raw byte strings for patterns if input is of byte data type
print(bool(re.search(rb'is', b'This is a sample string')))

# match the start of the input string
print(bool(re.search(r'\Ahi', 'hi hello\ntop spot')))


# match the start of a line
print(bool(re.search(r'^top', 'hi hello\ntop spot', flags=re.M)))


# match the end of strings
words = ['surrender', 'up', 'newer', 'do', 'era', 'eel', 'pest']
words_search = [w for w in words if re.search(r'er\Z', w)]
print(words_search)

# check if there's a whole line 'par'
print(bool(re.search(r'^par$', 'spare\npar\ndare', flags=re.M)))

