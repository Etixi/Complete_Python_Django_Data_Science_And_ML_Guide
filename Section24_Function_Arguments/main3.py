def my_fn(a, b):
    a = a + 1
    c = a + b
    return c

print(my_fn(13, 15))

def sum_nums(a, b):
    c = a + b
    return (c)

print(sum_nums(2, 5)) # 7
# print(sum_nums(2)) # Error
# print(sum_nums()) # Error

def sum_nums(*args):
    print(args)
    print(type(args))
    return sum(args)

print(sum_nums(2, 3, 7, 9))

def get_posts_info(name, posts_qty):
    info = f'{name} wrote {posts_qty} posts'
    return info

info = get_posts_info('Bogdan', 25)
print(info)

