from django.db import models

class VendorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()


