from django.db import models

# Create your models here.

class Ipdb(models.Model):
    ip = models.TextField(null=True, blank=True)
    post = models.TextField(null=True, blank=True)
    sl = models.IntegerField(null = True, blank = True, default = 0) 
    def __str__(self):
        return self.ip
    def incrementViewCount(self):
        self.sl += 1
        self.save()


class Iphomedb(models.Model):
    ip = models.TextField(null=True, blank=True)
    sl = models.IntegerField(null = True, blank = True, default = 0)

    def __str__(self):
        return self.ip
