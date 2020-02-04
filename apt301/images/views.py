from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apt301.images.serializers import ImageCreateSerializer


class ImageCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageCreateSerializer

