from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext as _


def storage_path(instance, filename):
    """
    Staging path with unique filename
    :param instance: image instance
    :param filename: original filename
    :return: storage path
    """
    return f'staging/{instance.name}'


class Image(models.Model):
    UNKNOWN = 0
    STAGING = 1
    SAVED = 2
    STATE = (
        (UNKNOWN, _('Image in unknown status')),
        (STAGING, _('Image is uploaded to S3 but staged')),
        (SAVED, _('Image is uploaded and associated with another resource')),
    )

    resource_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL)
    resource_id = models.PositiveIntegerField(null=True)
    resource = GenericForeignKey('resource_type', 'resource_id')
    image = models.ImageField(upload_to=storage_path)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=STATE, default=UNKNOWN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "images"
