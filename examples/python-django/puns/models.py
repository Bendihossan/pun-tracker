import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Pun(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    vote = models.BigIntegerField('vote count')

    def __unicode__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
