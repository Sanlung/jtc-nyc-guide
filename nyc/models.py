from django.db import models

class Borough(models.Model):
  borough = models.CharField(max_length=50)
