from django.db import models
from django.urls import reverse

class Blog(models.Model):
    bid=models.IntegerField(unique=True)
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=1000)
    author_id=models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comments(models.Model):
    cid=models.IntegerField()
    post_id=models.ForeignKey(Blog, to_field='bid', on_delete=models.CASCADE, related_name='comments')
    content=models.CharField(max_length=200)
    author_id=models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author_id} on blog with bid {self.post_id.bid}"
 
