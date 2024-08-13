from .models import Post
from rest_framework import serializers
from django.utils.translation import get_language
from django.utils.translation import gettext as _,activate,get_language


class PostSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()
    def get_post(self, obj):
        data = "Foysal",
        return _("my name is {}").format(data)
    class Meta:
        model = Post
        fields = ["title","body","post"]

    def to_representation(self, instance):
        # activate(get_language())
        # if get_language() == "sv":
        #     raise Exception("Custom exception created for sv")
        data = _("new data")
        ret = super().to_representation(instance)
        ret["language"] = get_language()
        ret["title"] = _(instance.title)
        ret["body"] = _(instance.body)
        ret["extra"] = _("this is extra data - {data}").format(data=data)
        return ret