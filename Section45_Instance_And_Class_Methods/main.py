print()
print("Practice - Inheriting Methods by the Instances" + "\n" +
      "==========================================================================")
print()

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes_qty = 0

    def like(self):
        self.likes_qty += 1

    @staticmethod
    def format_post(title, content):
        return (
            f"Post title : {title}\n"
            f"Post content : {content}"
        )

formatted_post = Post.format_post("My first post", "Some post content")
print(formatted_post)
#print(my_post.title)
#print(my_post.likes_qty)

#my_post.like()
#my_post.like()
#print(my_post.likes_qty)

#Post.like(my_post)
#print(my_post.likes_qty)