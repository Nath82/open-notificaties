from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import requests
from rest_framework import serializers


class CallbackURLValidator:
    code = "invalid-callback-url"
    message = _("De opgegeven callback URL kan geen notificaties ontvangen.")

    def __init__(self, url_field: str, auth_field: str):
        self.url_field = url_field
        self.auth_field = auth_field

    def __call__(self, attrs):
        url = attrs.get(self.url_field)
        auth = attrs.get(self.auth_field)

        response = requests.post(url, json={
            'kanaal': 'test',
            'hoofdObject': 'http://some.hoofdobject.nl/',
            'resource': 'some_resource',
            'resourceUrl': 'http://some.resource.nl/',
            'actie': 'create',
            'aanmaakdatum': '2019-01-01T12:00:00Z',
            'kenmerken': {}
        }, headers={'AUTHORIZATION': auth})

        if response.status_code != 204:
            raise serializers.ValidationError(self.message, code=self.code)


class CallbackURLAuthValidator:
    code = "no-auth-on-callback-url"
    message = _("De opgegeven callback URL is niet beveiligd met autorisatie.")

    def __call__(self, url):
        if not settings.TEST_CALLBACK_AUTH:
            return

        response = requests.post(url, json={
            'kanaal': 'test',
            'hoofdObject': 'http://some.hoofdobject.nl/',
            'resource': 'some_resource',
            'resourceUrl': 'http://some.resource.nl/',
            'actie': 'create',
            'aanmaakdatum': '2019-01-01T12:00:00Z',
            'kenmerken': {}
        })

        if response.status_code != 403:
            raise serializers.ValidationError(self.message, code=self.code)
