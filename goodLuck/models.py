from django.db import models
from django.core.urlresolvers import reverse
import sys

class Mymodel(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField ()
    randNum = models.IntegerField()
    bizz = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Mymodel:goodLuck_edit', kwargs={'pk': self.pk})

    