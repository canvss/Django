from django.http import request, HttpRequest, HttpResponse
from django.test import TestCase

from polls.captcha import Captcha
from polls.utils import gen_random_code


def test(request: HttpRequest) -> HttpResponse:
    print(request.session.get('userid'))

    # if request.session.get('userid'):
    #     print('yes')
    # else:
    #     print('No'
