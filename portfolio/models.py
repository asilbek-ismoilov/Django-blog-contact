from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Blog/image')
    description = models.TextField()
    
    published_date = models.DateTimeField(auto_now=True)

    author = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.title}  by {self.author}"


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"