import uuid
from django.db import models

from core.models.regions import State
from core.models.base import User, Base


class TitleTypes(models.IntegerChoices):
    MR = 1, 'MR.'
    MRS = 2, 'Mrs.'
    MS = 3, 'Ms.'
    DR = 4, 'Dr.'


class GenderTypes(models.IntegerChoices):
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'


class MaritalStatusTypes(models.IntegerChoices):
    MARRIED = 1, 'Married'
    UNMARRIED = 2, 'UnMarried'
    SEPARATED = 3, 'Separated'


class CategoryTypes(models.IntegerChoices):
    GENERAL = 1, 'General'
    EWS = 2, 'General(EWS)'
    SC = 3, 'SC'
    SEBC = 4, 'SEBC'
    ST = 5, 'ST'


class CertificateGivenByTypes(models.IntegerChoices):
    MAMALATDAR = 1, 'Mamalatdar'
    TDO = 2, 'T.D.O(Taluka Development Officer)'
    DC = 3, 'District Dy. Director (DC)'
    DO = 4, 'District Social Welfare Officer (DO)'


class Profile(Base):
    id = models.CharField(
        primary_key=True,
        max_length=36,
        editable=False,
        default=uuid.uuid4
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profiles',
        db_column='user_id',
    )
    unique_id = models.CharField(
        max_length=10,
        unique=True
    )
    title = models.PositiveSmallIntegerField(
        choices=TitleTypes.choices,
        default=TitleTypes.MR,
    )
    surname = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    father_husband = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    mother_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    gender = models.PositiveSmallIntegerField(
        choices=GenderTypes.choices,
        default=GenderTypes.MALE,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    marital_status = models.PositiveSmallIntegerField(
        choices=MaritalStatusTypes.choices,
        default=MaritalStatusTypes.UNMARRIED,
    )
    category = models.PositiveSmallIntegerField(
        choices=CategoryTypes.choices,
        default=CategoryTypes.GENERAL,
    )
    certificate_no = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    certificate_issued_date = models.DateField(
        null=True,
        blank=True
    )
    certificate_issued_from = models.ForeignKey(
        State,
        on_delete=models.DO_NOTHING,
        related_name='certificate_issued_from',
        db_column='certificate_issued_from_id',
        null=True,
        blank=True
    )
    non_creamy_layer_no = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    non_creamy_layer_date = models.DateField(
        null=True,
        blank=True
    )
    certificate_given_by = models.PositiveSmallIntegerField(
        choices=CertificateGivenByTypes.choices,
        default=None,
    )

    class Meta:
        db_table = 'profiles'
        verbose_name_plural = "Profiles"

    def __str__(self):
        if self.first_name and self.surname:
            return str(self.first_name) + str(self.surname)
        return self.id
