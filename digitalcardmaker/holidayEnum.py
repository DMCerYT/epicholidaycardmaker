from django.db import models

class HolidayType(models.IntegerChoices):
    PLACEHOLDER = 0, 'temp'
    CHRISTMAS = 1, 'christmas'
    NEWYEARS = 2, 'new years'
    THANKSGIVING = 3, 'thanksgiving'
    BIRTHDAYS = 4, 'birthdays'
