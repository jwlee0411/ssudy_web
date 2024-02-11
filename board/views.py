import os.path
import urllib
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ssudy_web import settings
import mimetypes
from .forms import PostForm, SearchForm
from .models import Post, Board, Search
import base64
import markdown
from django.utils.html import mark_safe
from django.core.paginator import Paginator


def handle_uploaded_file(f):
    fs = FileSystemStorage()
    filename = f.name
    message_bytes = filename.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    print(base64_message)
    fs.save(base64_message, f)
    return filename


def create(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            postForm = PostForm()
            board_title = Board.objects.filter()
            context = {'postForm': postForm, 'Board': board_title}
            return render(request, "board/create.html", context)

        elif request.method == "POST":
            postForm = PostForm(request.POST)

            if postForm.is_valid():
                post = postForm.save(commit=False)
                post.file1 = request.FILES.get("file1")
                post.file2 = request.FILES.get("file2")
                post.file3 = request.FILES.get("file3")
                post.file4 = request.FILES.get("file4")
                post.file5 = request.FILES.get("file5")
                post.save()
                return redirect('/board/read/' + str(post.id))

            else:
                print(postForm.errors)
                return redirect('/')
    else:
        return redirect('/')


def modify(request, bid):
    post = get_object_or_404(Post, id=bid)

    if post.name != request.user.username and not request.user.is_superuser:
        return redirect(f'/board/read/{bid}')

    if request.method == "GET":
        postForm = PostForm(instance=post)
        board_title = Board.objects.filter()
        context = {'postForm': postForm, 'Board': board_title, 'post': post}
        return render(request, "board/modify.html", context)

    elif request.method == "POST":
        postForm = PostForm(request.POST)

        if postForm.is_valid():
            post.title = postForm.cleaned_data["title"]
            post.contents = postForm.cleaned_data["contents"]
            post.board = postForm.cleaned_data["board"]
            post.name = postForm.cleaned_data["name"]

            # Update the files only if new files are provided
            new_file1 = request.FILES.get("file1")
            new_file2 = request.FILES.get("file2")
            new_file3 = request.FILES.get("file3")
            new_file4 = request.FILES.get("file4")
            new_file5 = request.FILES.get("file5")

            post.file_reset = postForm.cleaned_data["file_reset"]
            print(post.file_reset)

            if not post.file_reset :
                print("들어감")
                if new_file1:
                    post.file1 = new_file1
                if new_file2:
                    post.file2 = new_file2
                if new_file3:
                    post.file3 = new_file3
                if new_file4:
                    post.file4 = new_file4
                if new_file5:
                    post.file5 = new_file5
            else:
                post.file1 = ""
                post.file2 = ""
                post.file3 = ""
                post.file4 = ""
                post.file5 = ""

            post.save()
            return redirect('/board/read/' + str(post.id))

        else:
            return redirect('/')


def file_download(request, file_name):
    path = request.GET.get('path')
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    file_name = urllib.parse.quote(file_name.encode('utf-8'))


    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            print("시작")
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_path)[0])
            response['Content-Disposition'] = 'attachment; filename=%s' % file_name
            print(response['Content-Disposition'])
            return response

    else:
        message = '알 수 없는 오류가 발생했습니다.'
        return HttpResponse("<script>alert('" + message + "');history.back()'</script>")


def test(request):
    board_list = Post.objects.all()  # models.py Post 클래스의 모든 객체를 board_list에 담음
    # board_list 페이징 처리
    page = request.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(board_list, '1')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'board/list.html', {'page_obj': page_obj})


def search(request, name):
    if request.method == "GET":
        searchForm = SearchForm()
        posts = Post.objects.filter(title__contains=name).order_by('-id')
        page = request.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
        paginator = Paginator(posts, '20')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
        page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
        postImp = Post.objects.filter(board="중요 공지사항").order_by('-id')
        index = page_obj.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 2 if index >= 2 else 0
        if index < 2:
            end_index = 5 - start_index
        else:
            end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = list(paginator.page_range[start_index:end_index])
        context = {'posts': page_obj, 'result_list': page_obj, 'postImp': postImp, 'numbers': range(1, 10),
               'page_range': page_range, 'max_index': max_index - 2, 'search':1, 'searchForm':searchForm, 'name':name}


        return render(request, 'board/list.html', context)



    elif request.method == "POST":

        searchForm = SearchForm(request.POST)

        if searchForm.is_valid():



                search = searchForm.save(commit=False)

                search.save()

                return redirect('/board/search/' + search.search)


        else:

            return redirect(request.META['HTTP_REFERER'])

def get_queryset(self):
    search_keyword = self.request.GET.get('q', '')
    search_type = self.request.GET.get('type', '')
    notice_list = Notice.objects.order_by('-id')
    if search_keyword:
        if len(search_keyword) > 1:
            if search_type == 'all':
                search_notice_list = notice_list.filter(
                    Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                        writer__user_id__icontains=search_keyword))
            elif search_type == 'title_content':
                search_notice_list = notice_list.filter(
                    Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
            elif search_type == 'title':
                search_notice_list = notice_list.filter(title__icontains=search_keyword)
            elif search_type == 'content':
                search_notice_list = notice_list.filter(content__icontains=search_keyword)
            elif search_type == 'writer':
                search_notice_list = notice_list.filter(writer__user_id__icontains=search_keyword)

            return search_notice_list
        else:
            messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
    return notice_list


def get_context_data(self, **kwargs):
    search_keyword = self.request.GET.get('q', '')
    search_type = self.request.GET.get('type', '')

    if len(search_keyword) > 1 :
        context['q'] = search_keyword
    context['type'] = search_type

    return context


def list2(request, aid):
    if request.method == "GET":
        searchForm = SearchForm()
        board_title = Board.objects.all()

        for board in board_title:
            # tmp1 = board.main_id
            # tmp2 = board.title
            if aid == 0:
                posts = Post.objects.all().order_by('-id')
                title = "전체글보기"
                page = request.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
                paginator = Paginator(posts, '20')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
                page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

                postImp = Post.objects.filter(board="중요 공지사항").order_by('-id')

                index = page_obj.number - 1
                max_index = len(paginator.page_range)
                start_index = index - 2 if index >= 2 else 0
                if index < 2:
                    end_index = 5 - start_index
                else:
                    end_index = index + 3 if index <= max_index - 3 else max_index
                page_range = list(paginator.page_range[start_index:end_index])

                context = {'posts': page_obj, 'result_list': page_obj, 'postImp': postImp, 'title': title,
                           'numbers': range(1, 10), 'page_range': page_range, 'max_index': max_index - 2, 'searchForm':searchForm, 'all' : 1}
                return render(request, 'board/list.html', context)

            if aid == board.sub_id:
                posts = Post.objects.filter(board=board.board_title).order_by('-id')
                title = board.board_title
                page = request.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
                paginator = Paginator(posts, '20')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
                page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

                postImp = Post.objects.filter(board="중요 공지사항").order_by('-id')

                index = page_obj.number - 1
                max_index = len(paginator.page_range)
                start_index = index - 2 if index >= 2 else 0
                if index < 2:
                    end_index = 5 - start_index
                else:
                    end_index = index + 3 if index <= max_index - 3 else max_index
                page_range = list(paginator.page_range[start_index:end_index])

                context = {'posts': page_obj, 'result_list' : page_obj, 'postImp': postImp, 'title': title, 'numbers': range(1, 10), 'page_range':page_range, 'max_index':max_index-2, 'searchForm':searchForm, 'aid' : aid}
                return render(request, 'board/list.html', context)
    elif request.method == "POST":
        searchForm = SearchForm(request.POST)
        if searchForm.is_valid():

                search = searchForm.save(commit=False)
                search.save()
                return redirect('/board/search/'+search.search)

        else:
            return redirect(request.META['HTTP_REFERER'])


def read(request, bid):
    post = Post.objects.get(id=bid)
    if not request.user.is_authenticated:
        if "활동보고서" in post.board:
            return redirect("/")
        else:
            context = {'post': post}
            return render(request, 'board/read.html', context)
    else:
        user_groups = request.user.groups.all()
        group_name = user_groups.first().name
        if group_name == "숭실인" and "활동보고서" in post.board:
            return redirect("/")
        else:
            context = {'post': post}
            return render(request, 'board/read.html', context)


def delete(request, bid):
    post = get_object_or_404(Post, id=bid)

    if request.user.is_superuser:
        post = Post.objects.get(id=bid)
        post.delete()
        return redirect('/')


    if post.name != request.user.username:

        return redirect(f'/board/read/{bid}')
    else:
        post = Post.objects.get(id=bid)
        post.delete()
        return redirect('/')

