from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    pending = models.BooleanField(default=False)

    def __str__(self):
        return self.title
