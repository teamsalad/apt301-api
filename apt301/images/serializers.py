from rest_framework import serializers

from apt301.images.models import Image


class ImageCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = Image
        fields = ('id', 'image', 'name', 'state')
