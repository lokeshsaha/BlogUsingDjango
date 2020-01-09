from django.db import models

# Create your models here.


class post(models.Model):  # why underline
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.CharField( max_length=130)
    timeStamp = models.DateTimeField( blank=True)


def __str__(self):
    return 'message from ' + self.title + ' by' + self.author
