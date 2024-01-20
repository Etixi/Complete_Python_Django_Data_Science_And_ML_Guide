import re

# split based on one or more digit characters
print(re.split(r'\d+', 'Sample123string42with777numbers'))


# split based on digit or whitespace characters
print(re.split(r'[\d\s]+', '**1\f2\n3star\t7 77\r**'))


# to include the matching delimiter strings as well in the output
print(re.split(r'(\d+)', 'Sample123string42with777numbers'))

# multiple capture groups example
# note that the portion matched by b+ isn't present in the output
print(re.split(r'(a+)b+(c+)', '3.14aabccc42'))


# use non-capturing group if capturing is not needed
print(re.split(r'hand(?:y|ful)', '123handed42handy777handful500'))


# whole words that have at least one consecutive repeated character
words = ['effort', 'flee', 'facade', 'oddball', 'rat', 'tool']

words_split = [w for w in words if re.search(r'\b\w*(\w)\1\w*\b', w)]
print(words_split)

# re.Match object
print(re.search(r'so+n', 'too soon a song snatch'))


# retrieving entire matched portion, note the use of [0]
motivation = 'Doing is often better than thinking of doing.'
motivation_split = re.search(r'of.*ink', motivation)[0]
print(motivation_split)


# capture group example
purchase = 'coffee:100g tea:250g sugar:75g chocolate:50g'
m = re.search(r':(.*?)g.*?:(.*?)g.*?chocolate:(.*?)g', purchase)
# to get the matched portion of the second capture group
print(m[2])


# to get a tuple of all the capture groups
print(m.groups())

