import uuid
from django.db import models
from core.models.base import Base
from profiles.models.profiles import Profile


class ProfileDocuments(Base):
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
    user_image = models.ImageField(
        null=True,
        blank=True
    )
    signature_image = models.ImageField(
        null=True,
        blank=True
    )
    caste_certificate = models.ImageField(
        null=True,
        blank=True
    )
    non_creamy_layer_certificate = models.ImageField(
        null=True,
        blank=True
    )
    ews_certificate = models.ImageField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'profile_documents'
        verbose_name_plural = "Profile Documents"

    def __str__(self):
        return self.profile.user or self.id
