from apps.core.models import BaseModel
from django.db import models
from guardian.models import GroupObjectPermission


class LibraryIcon(BaseModel):
    name = models.CharField(max_length=255)
    svg_icon = models.TextField()

    class Meta:
        abstract = False
        db_table = "tblLibraryIcons"


class Library(BaseModel, GroupObjectPermission):
    name = models.CharField(max_length=255)
    base_dir = models.TextField()
    description = models.TextField(null=True, blank=True)
    svg_icon = models.ForeignKey(
        LibraryIcon, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = False
        db_table = "tblLibraries"
