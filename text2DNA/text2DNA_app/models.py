from django.db import models


class texttoDNA(models.Model):
    firstText = models.TextField()


class DNAtotext(models.Model):
    inDNA = models.TextField()
