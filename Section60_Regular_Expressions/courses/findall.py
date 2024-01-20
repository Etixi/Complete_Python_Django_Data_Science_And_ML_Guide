import re

# match 'par' with optional 's' at start and optional 'e' at end
print(re.findall(r'\bs?pare?\b', 'par spar apparent spare part pare'))

# numbers >= 100 with optional leading zeros
# use r'\b0*[1-9]\d{2,}\b' if possessive quantifiers isn't supported
print(re.findall(r'\b0*[1-9]\d{2,}\b', '0501 035 154 12 26 98234'))


# if multiple capturing groups are used, each element of output
# will be a tuple of strings of all the capture groups
print(re.findall(r'([^/]+)/([^/,]+),?', '2020/04,1986/Mar'))


# normal capture group will hinder ability to get whole match
# non-capturing group to the rescue
print(re.findall(r'\b\w*(?:st|in)\b', 'cost akin more east run'))


# useful for debugging purposes as well
print(re.findall(r':.*?:', 'green:3.14:teal::brown:oh!:blue'))
