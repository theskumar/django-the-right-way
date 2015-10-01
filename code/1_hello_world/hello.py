import sys

from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse

settings.configure(DEBUG=True, SECRET_KEY='super_secret',
                   ROOT_URLCONF=__name__, MIDDLEWARE_CLASSES=(),)


def index(request):
    return HttpResponse('Hello World')


urlpatterns = [
    url(r'^$', index)
]

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
