class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Post:
    count = 0

    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.likes = 0
        self.comments = []
        Post.count += 1

    def like(self):
        self.likes += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def __str__(self):
        return f"{self.user}: {self.content} Likes:{self.likes}"


class Comment:
    def __init__(self, user, text):
        self.user = user
        self.text = text

    def __str__(self):
        return f"{self.user}: {self.text}"


u1 = User("Tanu")
post = Post(u1, "Hello World")

post.like()
post.add_comment(Comment(u1, "Nice post"))

print(post)
for c in post.comments:
    print(c)

print("Total posts:", Post.count)