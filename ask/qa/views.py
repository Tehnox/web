from django.shortcuts import render
from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question(request, *args, **kwargs):
    arg_id = kwargs.get('id', -1)
    return HttpResponse(f'ID = {arg_id}')
