from django.http import HttpResponse
from datetime import datetime
import json 

def hello_world(request):
    now  = datetime.now().strftime('%b %mth, %Y - %H:%M %p')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))

def sorted_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type = 'application/json')


def say_hi(request,name,age):
    "return a greeting"
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}: Welcome to Platzigram'.format(name)

    return HttpResponse(message)

