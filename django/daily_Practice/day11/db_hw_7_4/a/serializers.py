# a- serializers.py

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = __(d)__


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = __(e)__


# (d) : ('id', 'title')
# (e) : ('id', 'title', 'content', 'created_at', 'updated_at')