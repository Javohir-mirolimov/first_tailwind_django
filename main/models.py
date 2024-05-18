from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Banner-image/')
    teg = models.ManyToManyField(to='Teg')



class Teg(models.Model):
    name = models.CharField(max_length=25)


class Activ_work(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo_image/')


class Frilanser(models.Model):
    name = models.CharField(max_length=25)
    tecnology = models.CharField(max_length=25)
    proects = models.IntegerField(default=0)
    star = models.FloatField(default=0)
    image = models.ImageField(upload_to='Image_frilanser/')


class Worktap(models.Model):
    image = models.ImageField(upload_to='worktap_image/')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)



class Work(models.Model):
    image = models.ImageField(upload_to='worktap_image/')
    title = models.CharField(max_length=25)


class Info(models.Model):
    logo = models.ImageField(upload_to='logo_image/')
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagramm = models.CharField(max_length=255)

