from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from . import providers
from .utils import register_social_user, get_social_app_credentials


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = providers.Google.validate(auth_token)

        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        google_cred = get_social_app_credentials("google")
        if user_data['aud'] != google_cred.client_id:
            raise AuthenticationFailed('Unauthorized activity detected')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(
            provider=provider,
            user_id=user_id,
            email=email,
            name=name,
            provider_data=user_data
        )


class FacebookSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        get_social_app_credentials("facebook")
        user_data = providers.Facebook.validate(auth_token)

        try:
            user_id = user_data.get('id')
            email = user_data.get('email')
            name = user_data.get('name')
            provider = 'facebook'

            return register_social_user(
                provider=provider,
                user_id=user_id,
                email=email,
                name=name,
                provider_data=user_data
            )

        except Exception as e:
            raise serializers.ValidationError(
                'The token  is invalid or expired. Please login again.'
            )