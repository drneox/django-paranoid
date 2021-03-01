from django_paranoid.models import ParanoidModel
from django.db import models


class MyModel(ParanoidModel):
    field = models.CharField(max_length=20)
