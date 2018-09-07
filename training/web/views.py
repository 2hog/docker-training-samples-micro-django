from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests


@login_required
def home(request):
    # Get greeting from Sinatra service
    greeting_basic_auth_credentials = requests.auth.HTTPBasicAuth(
        settings.GREETING_APP_USER,
        settings.GREETING_APP_PASSWORD,
    )
    greeting_response = requests.post(
        settings.GREETING_APP_URL,
        auth=greeting_basic_auth_credentials,
    )
    greeting = greeting_response.json()['greeting']

    # Get page content based on received greeting from Flask service
    content_basic_auth_credentials = requests.auth.HTTPBasicAuth(
        settings.CONTENT_APP_USER,
        settings.CONTENT_APP_PASSWORD,
    )
    content_response = requests.get(
        settings.CONTENT_APP_URL,
        auth=content_basic_auth_credentials,
        params={
            'greeting': greeting,
        },
    )

    # Render our page based on the received content
    content = content_response.text
    context = {
        'content': content,
    }

    return render(request, 'web/index.html', context=context)
