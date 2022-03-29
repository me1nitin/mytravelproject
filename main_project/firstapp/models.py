from django.db import models


class places(models.Model):
    name = models.CharField(max_length=250, default='SOME STRING')
    # name1 = models.CharField(max_length=300)
    ima = models.ImageField(blank=True, null=True, upload_to='pics_section')
    desc = models.TextField(null=True)


class team(models.Model):
    name = models.CharField(max_length=100, default='write name')
    ima = models.ImageField(blank=True, null=True, upload_to='pics_section')
    desc = models.TextField(null=True)

    def __str__(self):
        return self.name

# Create your models here.
# Create your models here.
