import uuid
from django.db import models
from core.models.base import Base
from core.models.regions import State, City
from profiles.models.profiles import Profile


class ContactDetails(Base):
    id = models.CharField(
        primary_key=True,
        max_length=36,
        editable=False,
        default=uuid.uuid4
    )
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        db_column='profile_id',
    )
    address = models.TextField(
        blank=True,
        null=True
    )
    state = models.ForeignKey(
        State,
        on_delete=models.DO_NOTHING,
        related_name='address_state',
        db_column='state_id',
        null=True,
        blank=True
    )
    district = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
        related_name='address_district',
        db_column='district_id',
        null=True,
        blank=True
    )
    taluka = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
        related_name='address_taluka',
        db_column='taluka_id',
        null=True,
        blank=True
    )
    mobile_no = models.IntegerField(
        blank=True,
        null=True,
    )
    email = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'contact_details'
        verbose_name_plural = "Contact Details"

    def __str__(self):
        return self.profile.user or self.id
