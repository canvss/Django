from django.test import TestCase

from polls.captcha import Captcha
from polls.utils import gen_random_code

if __name__ == '__main__':
    captcha_text = gen_random_code()
    print('验证码 = ' + captcha_text)
    image_data = Captcha.instance().generate(captcha_text)
    print(image_data)


