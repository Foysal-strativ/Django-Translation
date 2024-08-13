from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext as _

from core.models import Post
from core.serializers import PostSerializer


# Create your views here.
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TranslationView(APIView):
    def get(self, request, *args, **kwargs):
        data = _("Bangladesh 2.0")
        response = _("The current version of Bangladesh is - {version}").format(version=data)
        return Response(response)
