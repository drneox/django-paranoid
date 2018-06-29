
""" Sthis adds 'created_at', 'updated_at' and 'delete_at'  fields like a rail apps in django,
    also added soft delete method.
Copyright (c) 2018, Carlos Ganoza Plasencia
url: http://carlosganoza.com
"""

from datetime import datetime
from django.db import models


class LoggableModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def delete(self, hard=True, **kwargs):
        if type:
            super(LoggableModel, self).delete()
        else:
            self.deleted_at = datetime.now
            self.save()