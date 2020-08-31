from django.db import models


class MusicalWork(models.Model):
    iswc = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=250)
    lyrics = models.TextField(default='')
    duration_in_seconds = models.PositiveSmallIntegerField(default=180)


class Contributor(models.Model):
    name = models.CharField(max_length=250)
    musical_works = models.ManyToManyField(MusicalWork)
