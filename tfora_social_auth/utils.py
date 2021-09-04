import random
from . import signals
from .models import SocialApplication
from .exceptions import CustomException
from . models import User, SocialAccount


def generate_username(name):
    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def get_social_app_credentials(provider):
    """Query social app credentials from db provided by Providers (google,facebook)"""
    try:
        return SocialApplication.objects.get(provider=provider)
    except:
        raise Exception(
            f"{provider.title()} credentials not found in Social Applications")


def get_user_social_account(user, provider):
    """User have already registered.Checking corresponding provider"""
    try:
        return SocialAccount.objects.get(user=user, provider__provider=provider)
    except:
        raise CustomException({
            'status': 403,
            "message": "Login with your username and password"
        })


def register_social_user(provider, user_id, email, name, provider_data):
    if isinstance(email, type(None)):
        raise CustomException({
            'status': 403,
            "message": "E-mail cannot be blank"
        })

    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():

        social_account_user = get_user_social_account(
            filtered_user_by_email[0], provider)

        if provider == social_account_user.provider.provider:

            signals.user_logged_in.send(
                sender="social_user_login",
                provider=provider,
                user=filtered_user_by_email[0],
                provider_data=provider_data
            )

            token = filtered_user_by_email[0].get_token()

            auth_data = {
                'refresh': str(token),
                'access': str(token.access_token),
            }

            data = {
                "status": 200,
                "auth": auth_data,
                "message": "Logged in successfully"
            }

            return data
        else:

            raise CustomException({
                'status': 403,
                "message": 'Please continue your login using ' + social_account_user.provider.provider
            })
    else:

        if provider == 'google':
            first_name = provider_data['given_name']
            last_name = provider_data['family_name']

        elif provider == 'facebook':
            first_name = provider_data['first_name']
            last_name = provider_data['last_name']

        kwargs = {
            'username': generate_username(name),
            'email': email,
            "is_active": True,
            "first_name": first_name,
            "last_name": last_name
        }

        new_user = User.objects.create(**kwargs)
        new_user.set_unusable_password()
        new_user.save()

        signals.user_registered.send(
            sender="social_user_register",
            provider=provider,
            user=new_user,
            provider_data=provider_data
        )

        token = new_user.get_token()

        auth_data = {
            'refresh': str(token),
            'access': str(token.access_token)
        }

        data = {
            "status": 200,
            "auth": auth_data,
            "message": "Registered successfully"
        }
        return data