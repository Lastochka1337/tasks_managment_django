from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    status = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.name