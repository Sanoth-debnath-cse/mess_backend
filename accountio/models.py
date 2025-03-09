from autoslug import AutoSlugField

from django.db import models

from shared.base_model import BaseModel


class Mess(BaseModel):
    name=models.CharField(max_length=250)
    slug=AutoSlugField(populate_from="name",unique=True)
    total_mamber=models.PositiveIntegerField(default=1)
    image=models.ImageField(blank=True,null=True)
