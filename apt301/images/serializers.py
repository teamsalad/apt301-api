from rest_framework import serializers

from images.models import Image
from images.utils import unique_filename


class ImageCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    def create(self, validated_data):
        validated_data['name'] = unique_filename(validated_data['image'].name)
        validated_data['state'] = Image.STAGING
        return Image.objects.create(**validated_data)

    class Meta:
        model = Image
        fields = ('id', 'image', 'name', 'state',)
        read_only_fields = ('id', 'name', 'state',)
