from django.db import models


# create the DjangoClasses class with attributes
class DjangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default=0)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager() # interface through which dB query operations are provided to Django models

    def __str__(self):
        return self.title  # what the page displays when the class is clicked on
