from rest_framework.exceptions import APIException
from django.utils.encoding import force_text
from rest_framework import status


class CustomException(APIException):
    status_code = status.HTTP_200_OK
    default_detail = 'Something went wrong.'

    def __init__(self, detail, **kwargs):
        if detail is not None:
            self.detail = detail
        else:
            self.detail = {'detail': force_text(self.default_detail)}
        for key, value in kwargs.items():
            if key == "status_code":
                self.status_code = value
