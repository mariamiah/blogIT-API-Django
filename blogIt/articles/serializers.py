from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    id = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(view_name="articles:articles-detail", lookup_field="slug", read_only=True)


    def get_author(self, obj):
        return obj.author.username
    class Meta:
        model =  Article
        fields = ['url', 'id','title', 'body', 'publish','author','created', 'modified', 'status',]
