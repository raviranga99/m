from rest_framework.generics import (
ListAPIView,
)
from .serializers import (
PostListSerializer,
)
from blog.models import Post

class PostListAPIView(ListAPIView):
    serializer_class=PostListSerializer
    queryset=Post.objects.all()# queryset is a defoult obeject or overriding by get_queryset method
    """def get_queryset(self, *args, **kwargs):
       
        queryset_list = Post.objects.all() 
        return queryset_list"""

    
