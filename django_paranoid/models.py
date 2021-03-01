
""" This adds 'created_at', 'updated_at' and 'delete_at'  fields like a rail apps in django,
    also added soft delete method.
Copyright (c) 2018, Carlos Ganoza Plasencia
url: http://carlosganoza.com
"""

from django.utils.timezone import now
from django.db import models


class ParanoidModelManager(models.Manager):
    def get_queryset(self):
        return super(ParanoidModelManager, self).get_queryset().filter(deleted_at__isnull=True)


class ParanoidModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)
    objects = ParanoidModelManager()
    objects_with_deleted = models.Manager()

    class Meta:
        abstract = True

    def delete(self, hard=False, **kwargs):
        if hard:
            super(ParanoidModel, self).delete()
        else:
            self.deleted_at = now()
            self.save()

    def restore(self):
      self.deleted_at = None
      self.save()
