from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class SocialApplication(models.Model):
    AUTH_PROVIDERS = [
        ('facebook', 'Facebook'),
        ('google', 'Google')
    ]
    provider = models.CharField(max_length=128, choices=AUTH_PROVIDERS)
    name = models.CharField(max_length=128)
    client_id = models.CharField(
        max_length=256, help_text="App ID, or consumer key")
    client_secret = models.CharField(
        max_length=256, help_text="API secret, client secret, or consumer secret")

    def __str__(self):
        return self.name


class SocialAccount(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tfora_social_auth_account")
    provider = models.ForeignKey(SocialApplication, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
