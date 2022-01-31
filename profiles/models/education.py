import uuid
from django.db import models
from core.models.base import Base
from profiles.models.profiles import Profile


class DegreeTypes(models.IntegerChoices):
    X = 1, '10'
    XII = 2, '12'


class EducationDetails(Base):
    id = models.CharField(
        primary_key=True,
        max_length=36,
        editable=False,
        default=uuid.uuid4
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        db_column='profile_id',
    )
    degree = models.PositiveSmallIntegerField(
        choices=DegreeTypes.choices,
        default=None
    )
    institute_name = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    board_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    percentage = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )
    passing_year = models.DateField(
        null=True,
        blank=True
    )
    trials = models.IntegerField(
        default=0
    )
    document = models.ImageField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'education_details'
        verbose_name_plural = "Education Details"

    def __str__(self):
        return self.profile.user or self.id
