from django.http import HttpResponse

from http import HTTPStatus


def index(request):
    return HttpResponse('У меня получилось!', status_code=HTTPStatus.OK)


def second_page(request):
    return HttpResponse('А это вторая страница', status_code=HTTPStatus.OK)
