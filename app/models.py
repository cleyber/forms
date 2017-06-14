from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#@python_2_unicode_compatible
class User(models.Model):
    db_table = 'users'

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    def __str__(self):
        return self.name
