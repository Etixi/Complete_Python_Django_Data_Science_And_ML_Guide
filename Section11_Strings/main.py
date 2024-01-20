#  Created By Etienne KOA
print("===================== String Manipulation ==========================")
long_str = "This is a very long string"
long_str = 'This is a very long string'
long_str = 'It is a great day today'
long_str = "It is a great day today"
long_str = 'It \'s a great day today'
long_str = "This is a " \
            "very long " \
             "string"

long_str = "This is a very, very, very, " \
            "very, very, very, very, very, "\ 
             "very, very, very, very, very, very, very, very,very, very long string"

long_str = """
            This is a very, very, 
            very, very, very, very, very, very, 
            very, very, very, very, very, very, 
            very, very,very, very long string
            """
print(long_str)
print(type(long_str))
print(len(long_str))
print(type(long_str) == str)
print(id(long_str))

print("===================== String Methods ==========================")

my_comment = "This is my short comment"
print(my_comment)
print(len(my_comment))
print(my_comment.count(' '))
print(my_comment.count('is'))
print(my_comment[5])
print(my_comment[2:7]) # [2:9], [2:], [10:], [:-10], [3:-10], [:-1]
print(my_comment.find('short'))
print(my_comment.find('long'))
print(my_comment.find('long') == -1)
print(my_comment.split(' '))
print(my_comment.upper())
print(my_comment.lower())
print(dir(my_comment))
# long_comment = my_comment.replace('short', 'long')
my_comment = my_comment.replace('short', 'long')
print(my_comment)

