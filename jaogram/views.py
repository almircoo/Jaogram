"""Jaogram views"""
#django
from django.http import HttpResponse
#datetime utulities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Helooo, world! current server time is {now}'.format(now=now))
