from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from polls.models import Subject, Teacher, User
from polls.captcha import *
# Create your views here.
from polls.utils import *



def show_subjects(request):
    subjects = Subject.objects.all().order_by('no')
    return render(request,'subjects.html',{'subjects':subjects})

def show_teachers(request: HttpRequest) -> HttpResponse:
    if request.session.get('userid'):
        try:
            sno = int(request.GET.get('sno'))
            teachers = []
            if sno:
                subject = Subject.objects.only('name').get(no=sno)
                Teacher.objects.filter(subject=subject).order_by('no')
                return render(request,'teachers.html',{
                    'subject':subject,
                    'teachers':teachers
                })
        except(ValueError,Subject.DoesNotExist):
            return redirect('/')
    else:
        return redirect('/login')


def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    if request.session.get('userid'):
        try:
            tno = int(request.GET.get('tno'))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith('/praise'):
                teacher.good_count += 1
                count = teacher.good_count
            else:
                teacher.bad_count +=1
                count = teacher.bad_count
            teacher.save()
            data = {'code':20000,'mesg':'操作成功','count':count}
        except (ValueError,Teacher.DoesNotExist):
            data = {'code':20001,'mesg':'操作失败'}
    else:
        data = {'code':20002,'mesg':'请先登录'}
    return JsonResponse(data)


def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            password = gen_md5_digest(password)
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['userid'] = user.no
                request.session['username'] = user.username
                return render(request, 'header.html')
            else:
                hint = '用户名或密码错误'
        else:
            hint = '请输入有效的用户名和密码'
    return render(request, 'login.html', {'hint':hint})

#注销
def logout(request):
    #清空session对象
    request.session.flush()
    return redirect('/')


#验证码
def get_captcha(request: HttpRequest) -> HttpResponse:
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data,content_type='image/png')


def register(request: HttpRequest) -> HttpResponse:
    return render(request,'register.html')
