from django.db import models


class ChildProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    CLASS_CHOICES = [
        ('P1', 'Primary 1'),
        ('P2', 'Primary 2'),
        ('P3', 'Primary 3'),
        ('P4', 'Primary 4'),
        ('P5', 'Primary 5'),
        ('P6', 'Primary 6'),
        ('P7', 'Primary 7'),
        ('S', 'Secondary'),
        ('T', 'Tertiary'),
        ('u', 'University'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Child_class = models.CharField(max_length=10, choices=CLASS_CHOICES)
    is_orphan = models.BooleanField(default=False)
    Picture = models.ImageField(upload_to='children', blank=True, null=True)

    def __str__(self):
        return self.name
