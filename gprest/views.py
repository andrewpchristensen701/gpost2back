from rest_framework import viewsets
from gprest.models import Post
from gprest.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import JsonResponse
from django.middleware.csrf import get_token


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        like = Post.objects.get(pk=pk)
        like.net_votes += 1
        like.save()
        return Response({'status': 'liked!'})

    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        like = Post.objects.get(pk=pk)
        like.net_votes -= 1
        like.save()
        return Response({'status': 'disliked!'}) 

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})