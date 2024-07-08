from django.db import models

class event_scheduler(models.Model):
    i=models.IntegerField()
    name = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.i},{self.name},{self.date},{self.time},{self.description}"
