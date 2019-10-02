import re
from django.http import HttpResponse
from datetime import datetime


def home(request):
    return HttpResponse('hello django')


def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    match_object = re.match("[A-Za-z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = 'Friend'

    content = f'Hello there {clean_name}! Its {formatted_now}, bye!'
    return HttpResponse(content)
