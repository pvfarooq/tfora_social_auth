# tfora_social_auth

Easy django rest auth integration for social applications. (currently supports Google and Facebook)


## Quick Setup

Install package

	pip install tfora-social-auth


Add  `tfora_social_auth` app to INSTALLED_APPS in your django settings.py:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'tfora_social_auth',
    ...
]
```


	python manage.py migrate


#### Add URL patterns

```python
from tfora_social_auth.views import ( GoogleSocialAuthView, FacebookSocialAuthView )

urlpatterns = [
    path('social/google/', GoogleSocialAuthView.as_view()),
    path('social/facebook/', FacebookSocialAuthView.as_view()),
]

```


##### For Google login
- POST with "auth_token".
- Send an "idtoken" as from google to get user information

##### For Facebook login
- POST with "auth_token".
- Send an access token as from facebook to get user information

##### Extra token payload
You can add extra payload data to access token by the following method

```python
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserModel(AbstractUser):
    ...
    @staticmethod
    def get_token(user):
        token = RefreshToken.for_user(user)
        token["extra_key"] = "extra_value"
        return token
    ...

		
```
