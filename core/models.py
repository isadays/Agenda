from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import CharField


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_event = models.DateTimeField()
    date_create = models.DateTimeField(auto_now=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    #class Meta:
     #   db_table = 'event'


    def __str__(self):
        return self.title


    def get_date_event(self):
        return self.date_event.strftime('%m/%d/%Y , %H:%M')


    def get_date_input_event(self):
        return self.date_event.strftime('%Y-%m-%dT%H:%M')