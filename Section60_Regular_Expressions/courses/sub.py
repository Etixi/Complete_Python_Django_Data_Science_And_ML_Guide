import re
from math import factorial

# add something to the start of every line
ip_lines = "catapults\nconcatenate\ncat"
print(re.sub(r'^', '* ', ip_lines, flags=re.M))

# replace 'par' only at the start of a word
print(re.sub(r'\bpar', 'X', 'par spar apparent spare part'))


# same as: r'part|parrot|parent'
print(re.sub(r'par(en|ro)?t', 'X', 'par part parrot parent'))


# remove first two columns where : is delimiter
print(re.sub(r'\A([^:]+:){2}', '', 'apple:123:banana:cherry'))



# backreferencing in the replacement section
# remove any number of consecutive duplicate words separated by space
# use \W+ instead of space to cover cases like 'a;a<-;a'

print(re.sub(r'\b(\w+)( \1)+\b', r'\1', 'aa a a a 42 f_1 f_1 f_13.14'))


# add something around the matched strings
print(re.sub(r'\d+', r'(\g<0>0)', '52 apples and 31 mangoes'))


# swap words that are separated by a comma
print(re.sub(r'(\w+),(\w+)', r'\2,\1', 'good,bad 42,24'))


# example with both capturing and non-capturing groups
print(re.sub(r'(\d+)(?:abc)+(\d+)', r'\2:\1', '1000abcabc42 12abcd21'))



# using functions in the replacement section of re.sub()


numbers = '1 2 3 4 5'

def fact_num(n):
    return str(factorial(int(n[0])))

print(re.sub(r'\d+', fact_num, numbers))


# using lambda
print(re.sub(r'\d+', lambda m: str(factorial(int(m[0]))), numbers))


# examples for lookarounds
# change 'cat' only if it is not followed by a digit character
# note that the end of string satisfies the given assertion
# 'catcat' has two matches as the assertion doesn't consume characters

print(re.sub(r'cat(?!\d)', 'dog', 'hey cats! cat42 cat_5 catcat'))


# change whole word only if it is not preceded by : or -
print(re.sub(r'(?<![:-])\b\w+', 'X', ':cart <apple -rest ;tea'))


# extract digits only if it is preceded by - and followed by ; or :
print(re.findall(r'(?<=-)\d+(?=[:;])', '42 apple-5, fig3; x-83, y-20: f12'))


# words containing 'b' and 'e' and 't' in any order
words = ['sequoia', 'questionable', 'exhibit', 'equation']
print([w for w in words if re.search(r'(?=.*b)(?=.*e).*t', w)])

# match if 'do' is not there between 'at' and 'par'
print(bool(re.search(r'at((?!do).)*par', 'fox,cat,dog,parrot')))

# match if 'go' is not there between 'at' and 'par'
print(bool(re.search(r'at((?!go).)*par', 'fox,cat,dog,parrot')))