from django.db import models

# Create your models here.

class Note(models.Model):
    header  = models.CharField(max_length=700)
    main_text = models.CharField(max_length=700)
