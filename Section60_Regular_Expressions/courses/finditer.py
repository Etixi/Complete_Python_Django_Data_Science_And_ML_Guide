import re

# numbers < 350
m_iter = re.finditer(r'[0-9]+', '45 349 651 593 4 204 350')
m_numbers = [m[0] for m in m_iter if int(m[0]) < 350]
print(m_numbers)

# start and end+1 index of each matching portion
m_iter = re.finditer(r'so+n', 'song too soon snatch')
for m in m_iter:
    print(m.span())
