import json

print("============ Practice - Converting Python Objects to JSON =================")
# liste
my_nums = [10, 100, 5, 20]
my_nums_json = json.dumps(my_nums)
print(my_nums_json)
print(type(my_nums_json))

# tuple
my_nums = (10, 100, 5, 20)
my_nums_json = json.dumps(my_nums)

print(my_nums_json)
print(type(my_nums_json))

# set -> JSON (not possible)
# my_nums = {10, 100, 5, 20}
# my_nums_json = json.dumps(my_nums)
# TypeError: Object of type set is not JSON serializable


# dict

my_post = {
    'title': "My post",
    'content': "Post content",
    'likes_qty': 25,
    'author': {
        'username':'etienne123',
        'email':'e@gmail.com'
    },
    'metadata': (5, 7, 20)
}

my_post_json = json.dumps(my_post)
print(my_post_json)
print(type(my_post_json))

print("============ Practice - Converting from JSON to  Python Objects =================")

# JSON -> dict
my_post_dict = json.loads(my_post_json)
print(my_post_dict)
print(type(my_post_dict))
print(my_post_dict['likes_qty'])
# JSON -> list
my_list = json.loads('[10, "abc", null, [1, 2], {"name": "etienne"}]')
print(my_list)




# dict with function
def sum_fn(a, b):
    return a + b

my_math = {
    'title': "Math dict",
    'sum': sum_fn
}

# my_math_json = json.dumps(my_math)
# TypeError: Object of type set is not JSON serializable
# print(my_math_json)

print("============ Practice - Formatting Dictionaries using JSON =================")

my_dict = {
    'name': 'etienne',
    'is_instructor': 'true'
}

print(my_dict)
my_dict_json = json.dumps(my_dict, indent=2)

file = open('../Section53_JavaScript_Object_Notation(JSON)/files/test.txt', 'w')
file.write(my_dict_json)