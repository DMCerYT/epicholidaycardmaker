import uuid

from django.db import models
from . import holidayEnum
# - this imports the Holiday Enums

# Create your models here.
class Card(models.Model):
    recipient = models.CharField(max_length=50)
    # ^ Will contain the recipient's name
    sender = models.CharField(max_length=50)
    # ^ Will contain the sender's name

    message = models.TextField()
    # ^ Contains a little message from the sender

    holidayType = models.IntegerField(choices=holidayEnum.HolidayType)
    # ^ ALlows us to choose from a particular holiday set

    created_at = models.DateTimeField(auto_now_add=True)
    # ^ Here we can see when the card was created

    card_hash_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.recipient} - {self.sender} - [ID: {self.card_hash_id}] - ({self.holidayType})"
