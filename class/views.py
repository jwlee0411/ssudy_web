from django.core.mail import EmailMessage
from urllib.parse import urlparse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserve, Check
from manager.models import Email
from django.core.files.storage import FileSystemStorage
from .forms import ReserveForm, CheckForm
import string
import random
from datetime import datetime
from django.core.paginator import Paginator
from ssudy_web import settings
import mimetypes
# Create your views here.

def check_result_3(request):
    context = {'valid': 'no'}
    return render(request, 'class/check_result.html', context)


def check_result_2(request, checksum):
    context = {'valid': 'no'}
    return render(request, 'class/check_result.html', context)


def check_result(request, id, checksum):
    try:
        post = Reserve.objects.get(id=id)
    except:
        context = {'valid': 'no'}
    else:
        if post.checksum == checksum:
            context = {'post': post, 'valid': 'yes'}
        else:
            context = {'post': post, 'valid': 'no'}

    return render(request, 'class/check_result.html', context)


def check(request):
    return render(request, 'class/check.html')


def class_print(request, id, checksum):
    post = Reserve.objects.get(id=id)
    # 현재 날짜를 가져옵니다.
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y년 %m월 %d일")
    context = {'post': post, 'date':formatted_date}
    if post.checksum == checksum:
        if post.stu != "" and post.dy != "":
            return render(request, 'class/print.html', context)
        else:
            return redirect('/')
    else:
        return redirect('/')


def read(request, id):
    post = Reserve.objects.get(id=id)
    context = {'post': post}
    for group in request.user.groups.all():
        if group.name == "동아리연합회" or "학생서비스팀":
            return render(request, 'class/read.html', context)

    return redirect('/')

def confirm(request, id):
    post = Reserve.objects.get(id=id)
    print('들어옴')
    full_url = request.build_absolute_uri()
    parsed_url = urlparse(full_url)
    domain = f"{parsed_url.scheme}://{parsed_url.netloc}"

    for group in request.user.groups.all():
        if group.name == "동아리연합회" :
            post.dy = request.user.first_name
            post.save()
        if group.name == "학생서비스팀":
            post.stu = request.user.first_name
            email_sendto = [str(post.email)]
            email2 = EmailMessage(
                '[동아리연합회] 교내이용시설 승인완료(학생서비스팀)',  # 이메일 제목
                '신청하신 교내이용시설의 학생서비스팀 승인이 완료되었습니다.' + '\n아래 링크에서 장소사용신청서를 출력해서 관리팀에서 최종 승인을 받으시면 해당 일시에 교내이용시설 사용이 가능합니다. \n\n' + domain+'/class/print/'
                + str(post.id) + "-" + str(post.checksum) + '\n\n본 이메일은 발신전용으로 회신이 되지 않습니다.',
                to=email_sendto  # 받는 이메일
            )
            email2.send()
            post.save()

    return redirect('/class/read/'+ str(id))



def create(request):
    for group in request.user.groups.all():
        if group.name == "동아리연합회" or group.name == "동아리" :
            if request.method == "GET":
                postForm = ReserveForm()
                board_title = Reserve.objects.filter()
                context = {'postForm': postForm, 'Board': board_title}
                return render(request, "class/create.html", context)

            elif request.method == "POST":
                postForm = ReserveForm(request.POST)

                if postForm.is_valid():
                    rand_str = ""
                    for i in range(10):
                        rand_str += str(random.choice(string.ascii_uppercase + string.digits))
                    post = postForm.save(commit=False)
                    post.file1 = request.FILES.get("file1")
                    post.name = request.user.first_name
                    post.club = request.user.username
                    post.phone_number = request.user.phone_number
                    post.email = request.user.email + request.user.email2
                    post.checksum = rand_str
                    post.save()

                    full_url = request.build_absolute_uri()
                    parsed_url = urlparse(full_url)
                    domain = f"{parsed_url.scheme}://{parsed_url.netloc}"

                    admin_email = Email.objects.filter()


                    email_sendto = [str(request.user.email + request.user.email2)]
                    email2 = EmailMessage(
                        '[동아리연합회] 교내이용시설 신청완료',  # 이메일 제목
                        '교내이용시설 이용 신청이 완료되었습니다.' + '\n처리 상황은 아래 링크에서 확인하실 수 있습니다. \n\n' + domain+'/class/read/'+str(post.id)  + '\n\n본 이메일은 발신전용으로 회신이 되지 않습니다.',
                        to=email_sendto # 받는 이메일
                    )
                    email2.send()


                    email_sendto3 = [admin_email[len(admin_email)-1].email1]
                    email3 = EmailMessage(
                        '교내이용시설 승인 요청',  # 이메일 제목
                        '교내이용시설 이용 신청이 들어왔습니다.' + '\n아래 링크에서 확인 후 승인해주시기 바랍니다. \n\n' + domain + '/class/read/' + str(
                            post.id)  + '\n\n본 이메일은 발신전용으로 회신이 되지 않습니다.',
                        to=email_sendto3  # 받는 이메일
                    )
                    email3.send()




                    return redirect('/class/read/' + str(post.id))

                else:
                    return redirect('/')
    else:
        return redirect('/')

def delete(request, id):
    post = get_object_or_404(Reserve, id=id)

    if request.user.is_superuser:
        post = Reserve.objects.get(id=id)
        post.delete()
        return redirect('/class/list')

    if post.club != request.user.username:
        return redirect('/class/list')

    else:
        post = Reserve.objects.get(id=id)
        post.delete()
        return redirect('/class/list')


def list2(request):
    for group in request.user.groups.all():
        if group.name == "동아리연합회" or group.name == "학생서비스팀" :
            posts = Reserve.objects.all().order_by('-id')
            page = request.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
            paginator = Paginator(posts, '20')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
            page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

            index = page_obj.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 2 if index >= 2 else 0
            if index < 2:
                end_index = 5 - start_index
            else:
                end_index = index + 3 if index <= max_index - 3 else max_index
            print(paginator.page_range)
            page_range = list(paginator.page_range[start_index:end_index])

            context = {'posts': page_obj, 'result_list': page_obj,
                       'numbers': range(1, 10), 'page_range' : page_range, 'max_index' : max_index - 2}

            return render(request, 'class/list.html', context)

        elif group.name == "동아리":
            posts = Reserve.objects.filter(club=request.user.username).order_by('-id')
            page = request.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
            paginator = Paginator(posts, '20')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
            page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

            index = page_obj.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 2 if index >= 2 else 0
            if index < 2:
                end_index = 5 - start_index
            else:
                end_index = index + 3 if index <= max_index - 3 else max_index
            page_range = list(paginator.page_range[start_index:end_index])

            context = {'posts': page_obj, 'result_list': page_obj,
                       'numbers': range(1, 10), 'page_range' : page_range, 'max_index' : max_index - 2}

            return render(request, 'class/list.html', context)

    return redirect('/')