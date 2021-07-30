from django.dispatch import Signal, receiver
from .models import User, SocialAccount, SocialApplication
user_registered = Signal()


@receiver(user_registered)
def create_social_account(user, provider, provider_data, **kwargs):
    social_account = SocialAccount.objects.filter(
        user=user, provider__provider=provider)

    if not social_account.exists():
        app = SocialApplication.objects.get(provider=provider)
        SocialAccount.objects.create(user=user, provider=app)
