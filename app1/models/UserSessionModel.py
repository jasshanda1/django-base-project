from django.db import models
from .UserModel import User


class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    device_id = models.CharField(max_length=100, null = True, blank= True)
    token = models.CharField(max_length=560, null = True, blank= True)
    device_type = models.CharField(max_length=20,  null = True, blank= True)
    device_token = models.CharField(max_length=200,  null = True, blank= True)
    app_version = models.CharField(max_length=60, null= True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.device_id)

    class Meta:
        db_table = 'user_session'
        indexes = [
            models.Index(fields=['id'])
        ]
