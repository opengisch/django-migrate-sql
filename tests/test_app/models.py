from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    rating = models.IntegerField(null=True, blank=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return "Book [{}]".format(self.name)
