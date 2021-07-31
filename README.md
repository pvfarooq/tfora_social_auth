# tfora_social_auth


###### Easy django rest auth integration for social applications (currently supports google and facebook)

### Installation

`pip install tfora-social-auth`



##### INSTALLED_APPS = [

`  'tfora_social_auth'
`

###### ]



`python manage.py migrate
`



##### in urls

`from tfora_social_auth.views import (GoogleSocialAuthView,FacebookSocialAuthView)
`
##### urlpatterns = [

`  path('google/', GoogleSocialAuthView.as_view()),
`

`path('facebook/', FacebookSocialAuthView.as_view()),
`
##### ]



### For Google login
`POST with "auth_token"
Send an "idtoken" as from google to get user information
`
### For Facebook login
`POST with "auth_token"
Send an access token as from facebook to get user information`


