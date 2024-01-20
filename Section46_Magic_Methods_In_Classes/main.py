class Post:
    def __init__(self, title):
        self.title = title

    def __add__(self, other):
        return f"{self.title} {other.title}"

    def __eq__(self, other):
        return self.title == other.title

first_post = Post("This is first post")
second_post = Post("This is second post")
same_post_as_first = Post("This is first post")

print(first_post + second_post)
print(first_post == same_post_as_first)
print(first_post == second_post)