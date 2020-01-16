from rest_framework.serializers import HyperlinkedModelSerializer
from gprest.models import Post


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['is_boast',
                  'content',
                  'upvotes',
                  'downvotes',
                  'post_date',
                  'net_votes', 
                  'id']