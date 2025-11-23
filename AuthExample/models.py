from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
#TEACHER ROLE
cohort_name=(
    ('ec 1','EC 1'),
    ('ec 2', 'EC 2'),
    ('ec 3','EC 3'),
    ('ec 4','EC 4'),
)
class cohort(models.Model):
    id = models.AutoField(primary_key=True)
    cohort_name = models.CharField(max_length=10,choices=cohort_name, default=False)    

    def __str__(self):
        return self.cohort_name

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    cohort =  models.CharField(max_length=10, choices=cohort_name, default=False)



class module(models.Model):
    id = models.AutoField(primary_key=True)
    module_name = models.TextField()

    def __str__(self):
        return self.module_name


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=10, default=True)
    max_seating = models.IntegerField()

    def __str__(self):
        return self.room_name


class_types = (
    ('lecture','Lecture'),
    ('lab', 'Lab'),
    ('seminar','Seminar'),
)

activity_types=(('study','study'),
                ('meeting','meeting'),
                ('practice','practice'),)

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    class_types = models.CharField(max_length=10, choices=class_types, default=False)
    activity_types = models.CharField(max_length=10, choices=activity_types, default=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    module = models.ForeignKey(module, on_delete=models.CASCADE)
    cohort = models.ForeignKey(cohort, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)