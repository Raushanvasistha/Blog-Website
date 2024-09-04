from rest_framework import serializers
from blogsapp.models import Blog,Comments

class blogSerializers(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['bid','title','content','author_id','created_at','updated_at']


class commentsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields=['cid','post_id','content','author_id','created_at']
