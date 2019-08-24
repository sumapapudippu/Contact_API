# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Person(TimeStampedModel):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    
    @property
    def details(self):
        return self.detail_set.all()  

    def __str__(self):
        return self.first_name


class Detail(TimeStampedModel):
    name = models.ForeignKey(Person, related_name='details', on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=30)
    email = models.EmailField()
    Address = models.TextField()
    
    def __str__(self):
        return self.email