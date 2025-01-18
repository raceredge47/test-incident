from django.db import models
from user.models import User
# Create your models here.


class Incident(models.Model):
    LOW = 'Low'
    HIGH = 'High'
    MEDIUM = 'Medium'
    PRIORITY = (
        (LOW, 'Low'),
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
    )

    OPEN = 'Open'
    CLOSED = 'Closed'
    IN_PROGRESS = 'IN-Progress'

    STATUS = (
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
        (IN_PROGRESS, 'IN-Progress')
    )
    incident_details = models.TextField()
    status = models.CharField(choices=STATUS)
    priority = models.CharField(choices=PRIORITY)
    entity = models.CharField(choices=User.ENTITY)
    reported_date = models.DateTimeField(auto_now=True)
    reporter_name = models.CharField(max_length=70, db_index=True)
    incident_id = models.CharField(max_length=12, db_index=True, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.incident_id