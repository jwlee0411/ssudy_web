from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import ReserveNewForm
from .models import Reserve_new

from manager.models import AddClass, ClassSetting
from django.core.paginator import Paginator

from django.db.models import IntegerField
from django.db.models.functions import Cast

def list_new_admin(request):
    room = AddClass.objects.all()

    today = datetime.now()
    today_zero = today.replace(hour=0, minute=0, second=0, microsecond=0)
    formatted_date = today_zero.strftime("%Y-%m-%d")
    posts = Reserve_new.objects.filter(reserve_date=today_zero).annotate(
        reserve_time_int=Cast('reserve_time', IntegerField())).order_by('-reserve_date', 'reserve_time_int')
    print(posts)



    numbers = list(range(0, 13))
    reserve_dict = {}

    for i in numbers:
        if i==0:
            reserve_dict.clear()
        reserve_dict[str(i)] = []
        for rm in room:
            reserved = False
            for post in posts:
                if rm.name == post.room and str(i)==post.reserve_time:
                    reserved=True
                    if request.user.is_superuser :
                        if post.confirm:
                            result = post.user_name+" / "+post.user_id+" / "+str(post.user_tel)
                        else :
                            result = post.user_name + " / " + post.user_id + " / " + str(post.user_tel) + "승인대기"
                        reserve_dict[str(i)].append(str(result))
                    else:
                        if post.confirm:
                            reserve_dict[str(i)].append(post.user_name)
                        else:
                            reserve_dict[str(i)].append("(승인 대기 중)")
            if not reserved:
                reserve_dict[str(i)].append("")

    print(reserve_dict)


    context = {'room':room, 'posts':posts, 'numbers':list(map(str, range(1, 14))), 'date':formatted_date, 'reserve_dict':reserve_dict}
    return render(request, 'book/list_new_admin.html', context)

def list_new_admin2(request, date):
    room = AddClass.objects.all()


    posts = Reserve_new.objects.filter(reserve_date=date).annotate(
        reserve_time_int=Cast('reserve_time', IntegerField())).order_by('-reserve_date', 'reserve_time_int')

    print(posts.values())

    numbers = list(range(0, 13))
    reserve_dict = {}

    for i in numbers:
        if i==0:
            reserve_dict.clear()
        reserve_dict[str(i)] = []
        for rm in room:
            reserved = False
            for post in posts:
                if rm.name == post.room and str(i)==post.reserve_time:

                    reserved = True
                    if request.user.is_superuser:
                        if post.confirm:
                            result = post.user_name + " / " + post.user_id + " / " + str(post.user_tel)
                        else:
                            result = "(승인대기) " + post.user_name + " / " + post.user_id + " / " + str(post.user_tel)
                        reserve_dict[str(i)].append(str(result))
                    else:
                        if post.confirm:
                            reserve_dict[str(i)].append(post.user_name)
                        else:
                            reserve_dict[str(i)].append("(승인 대기 중)")
            if not reserved:
                reserve_dict[str(i)].append("")

    print(reserve_dict)


    context = {'room':room, 'posts':posts, 'numbers':list(map(str, range(1, 14))), 'date':date, 'reserve_dict':reserve_dict}
    return render(request, 'book/list_new_admin.html', context)





def list_new(request):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            posts = Reserve_new.objects.filter().annotate(
            reserve_time_int=Cast('reserve_time', IntegerField())).order_by('-reserve_date', 'reserve_time_int')
        else:
            posts = Reserve_new.objects.filter(user_name=request.user.username).annotate(
                reserve_time_int=Cast('reserve_time', IntegerField())).order_by('-reserve_date', 'reserve_time_int')

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


        room = AddClass.objects.all()

        today = datetime.now()
        today_zero = today.replace(hour=0, minute=0, second=0, microsecond=0)

        class_range = ClassSetting.objects.all()
        user_groups = request.user.groups.all()
        group_name = user_groups.first().name

        if group_name == "숭실인":
            time_end = int(class_range[len(class_range) - 1].stu_end)-1
        else:
            time_end = int(class_range[len(class_range) - 1].club_end)-1

        today_fin = today_zero + timedelta(days=time_end)

        context = {'posts': page_obj, 'result_list': page_obj,
                       'numbers': range(1, 10), 'page_range' : page_range, 'max_index' : max_index - 2, 'room' : room, 'name':"", 'today':today_fin}

        return render(request, 'book/list_new.html', context)


    return redirect('/')

def list_new2(request, date):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            posts = Reserve_new.objects.filter(reserve_date=date).annotate(
                reserve_time_int=Cast('reserve_time', IntegerField())).order_by('reserve_time_int')
        else:
            posts = Reserve_new.objects.filter(user_name=request.user.username, reserve_date=date).annotate(
                reserve_time_int=Cast('reserve_time', IntegerField())).order_by('reserve_time_int')



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
        room = AddClass.objects.all()

        today = datetime.now()
        today_zero = today.replace(hour=0, minute=0, second=0, microsecond=0)

        class_range = ClassSetting.objects.all()
        user_groups = request.user.groups.all()
        group_name = user_groups.first().name

        if group_name == "숭실인":
            time_end = int(class_range[len(class_range) - 1].stu_end) - 1
        else:
            time_end = int(class_range[len(class_range) - 1].club_end) - 1

        today_fin = today_zero + timedelta(days=time_end)

        context = {'posts': page_obj, 'result_list': page_obj,
                       'numbers': range(1, 10), 'page_range' : page_range, 'max_index' : max_index - 2, 'room' : room, 'name':"", 'today':today_fin}

        return render(request, 'book/list_new.html', context)




    return redirect('/')


def list_new3(request, room):
    if request.user.is_authenticated :
        if request.user.is_superuser:
            posts = Reserve_new.objects.filter(room=room).annotate(
                reserve_time_int=Cast('reserve_time', IntegerField())
            ).order_by('-reserve_date', 'reserve_time_int')
        else:
            posts = Reserve_new.objects.filter(user_name=request.user.username, room=room).annotate(
                reserve_time_int=Cast('reserve_time', IntegerField())
            ).order_by('-reserve_date', 'reserve_time_int')

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

        room_all = AddClass.objects.all()

        today = datetime.now()
        today_zero = today.replace(hour=0, minute=0, second=0, microsecond=0)

        class_range = ClassSetting.objects.all()
        user_groups = request.user.groups.all()
        group_name = user_groups.first().name

        if group_name == "숭실인":
            time_end = int(class_range[len(class_range) - 1].stu_end) - 1
        else:
            time_end = int(class_range[len(class_range) - 1].club_end) - 1

        today_fin = today_zero + timedelta(days=time_end)

        context = {'posts': page_obj, 'result_list': page_obj,
                       'numbers': range(1, 10), 'page_range' : page_range, 'max_index' : max_index - 2, 'room':room_all, 'name':room, 'today':today_fin}

        return render(request, 'book/list_new.html', context)




    return redirect('/')



def cancel_new(request, aid):
    if request.user.is_authenticated:
        if request.user.is_superuser:

            posts = Reserve_new.objects.filter(id=aid)
            for post in posts:
                post.delete()
            return redirect('/book/list_new')
        else:
            posts = Reserve_new.objects.filter(id=aid)
            for post in posts:
                date_obj = post.reserve_date
                today = datetime.now()
                today_zero = today.replace(hour=0, minute=0, second=0, microsecond=0)
                day_difference = date_obj - today_zero

                class_range = ClassSetting.objects.all()
                user_groups = request.user.groups.all()
                group_name = user_groups.first().name

                if group_name == "숭실인":
                    time_start = int(class_range[len(class_range) - 1].stu_start)
                    time_end = int(class_range[len(class_range) - 1].stu_end)
                else:
                    time_start = int(class_range[len(class_range) - 1].club_start)
                    time_end = int(class_range[len(class_range) - 1].club_end)

                if day_difference.days < time_end :
                    return redirect('/book/list_new')

                post.delete()
                return redirect('/book/list_new')


def confirm_new(request, aid):
    if request.user.is_superuser:
        posts = Reserve_new.objects.filter(id=aid)
        for post in posts:
            post.confirm = True
            post.save()
            return redirect('/book/list_new')



def read_new(request, bid):
    post = Reserve_new.objects.get(id=bid)
    if not request.user.is_authenticated:
        return redirect('./')
    elif request.user.is_superuser:
        context = {'post': post}
        return render(request, 'book/read_new.html', context)
    else:
        if post.user_name == request.user.username:
            context = {'post': post}
            return render(request, 'book/read_new.html', context)

    return redirect('/')





def create_new_main(request):
    class_range = ClassSetting.objects.all()
    room= AddClass.objects.all()
    context = {'room':room, 'class_range' : class_range[len(class_range)-1]}
    return render(request, 'book/create_new_main.html', context)

def create_new(request, room):
    class_range = ClassSetting.objects.all()
    context = {'room_name':room, 'class_range' : class_range[len(class_range)-1]}
    return render(request, 'book/create_new.html', context)

def create_new_error(request, room):
    return redirect('/book/create_new/'+room)



def create_new2(request, room, date):
    reserve_value = []
    reserve_list = Reserve_new.objects.filter(reserve_date=date, room=room)
    for i in reserve_list:
        reserve_value.append(i.reserve_time)
    reserve_value.sort()
    print(reserve_value)
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    weekday = date_obj.weekday()
    context = {'reserve_value': reserve_value, 'date': date, 'weekday':weekday, 'room_name':room}
    return render(request, 'book/create_new_2.html', context)

def create_new3(request, room, date, time):
    if request.user.is_authenticated:
        if request.method == "GET":
            reserveForm = ReserveNewForm()

            context = {'reserveForm': reserveForm, 'room_name':room, 'date':date, 'reserve_time':time}
            return render(request, "book/create_new_3.html", context)

        elif request.method == "POST":
            print("post")
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            today = datetime.now()
            today_zero = today.replace(hour=0, minute=0, second=0, microsecond=0)
            day_difference = date_obj - today_zero
            weekday = date_obj.weekday()
            print(day_difference)
            class_range = ClassSetting.objects.all()
            user_groups = request.user.groups.all()
            group_name = user_groups.first().name

            if group_name == "숭실인":
                time_start = int(class_range[len(class_range) - 1].stu_start)
                time_end = int(class_range[len(class_range) - 1].stu_end)
            else:
                time_start = int(class_range[len(class_range) - 1].club_start)
                time_end = int(class_range[len(class_range) - 1].club_end)

            if time_start <= today_zero.day:
                last_day_of_month = datetime(today.year, today.month + 1, 1) - timedelta(days=1) - today_zero.day
            else:
                last_day_of_month = datetime(today.year, today.month + 1, 1) - timedelta(days=1)

            if weekday is "0":
                print('weekday')
                return redirect('/book/create_new/' + str(room) + '/' + str(date))

            if last_day_of_month < date_obj:
                print('dates' + str(day_difference.days))
                return redirect('/book/create_new/' + str(room) + '/' + str(date))

            if day_difference.days < time_end:
                print('dates' + str(day_difference.days))
                return redirect('/book/create_new/' + str(room) + '/' + str(date))

            reserve_list = Reserve_new.objects.filter(reserve_date=date)
            for i in reserve_list:
                print(i.reserve_time)
                print(time)
                if str(i.reserve_time) == str(time) and i.room == room:
                    return redirect('/book/create_new/' + str(room) + '/' + str(date))

            room_db = AddClass.objects.filter(name=room)
            confirm = True
            for rm in room_db:
                confirm = rm.confirm

            reserveForm = ReserveNewForm(request.POST)
            if reserveForm.is_valid():
                search = reserveForm.save(commit=False)

                search.user_id = request.user.first_name
                search.user_name = request.user.username
                search.reserve_date = date
                search.reserve_time = str(time)
                search.user_email = request.user.email
                search.user_tel = request.user.phone_number
                search.room = room
                search.confirm = not confirm
                search.save()
                return redirect('/book/list_new')
            else:
                error_messages = reserveForm.errors
                print(error_messages)

    else:
        return redirect('/book/create_new/'+str(date))


def create_new_admin(request):
    if request.method == "GET":
        reserveForm = ReserveNewForm()
        room = AddClass.objects.all()
        context = {'room': room, 'reserveForm':reserveForm}
        return render(request, 'book/create_new_admin.html', context)
    elif request.method == "POST":
        reserveForm = ReserveNewForm(request.POST)
        if reserveForm.is_valid():
            reserve = reserveForm.save(commit=False)
            reserve.confirm = True
            reserve.save()
            return redirect('/book/list_new')



