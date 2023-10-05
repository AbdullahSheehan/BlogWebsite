from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_name')
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=500, unique=True)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to='blogImages/', verbose_name="Image")

    class Meta:
        ordering=['-publish']

    def __str__(self):
        return self.title + " by " + self.author.last_name
class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_name')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker_name')

    def __str__(self):
        return str(self.user)+" likes "+str(self.blog)
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentator_name')
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return str(self.user)+" commented on "+str(self.blog)