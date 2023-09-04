from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name
