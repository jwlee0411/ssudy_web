from django.shortcuts import render
from board.models import Post

from manager.models import Popup, Front, MainBoard, Terms

from django.core.paginator import Paginator


def home(request):
    main_boards = MainBoard.objects.filter()

    main_board_1 = main_boards[len(main_boards) - 1].board1

    main_board_2 = main_boards[len(main_boards) - 1].board2

    popups = Popup.objects.filter()
    fronts = Front.objects.filter()

    board1 = Post.objects.filter(board=main_board_1)
    board2 = Post.objects.filter(board=main_board_2)

    if len(board1)>=4 :
        board_final_1 = board1[len(board1)-4:][::-1]
    else:
        board_final_1 = board1[::-1]
    if len(board2) >= 4 :
        board_final_2 = board2[len(board2)-4:][::-1]
    else:
        board_final_2 = board2[::-1]

    context = {'board1': board_final_1, 'board2': board_final_2, 'popup': popups[len(popups) - 1], 'front': fronts[len(fronts) - 1],
               'main_board': main_boards[len(main_boards) - 1]}
    # context = {'board1': board1, 'board2': board2, 'popup': "1234"}
    return render(request, 'home/index.html', context)


def terms(request):
    file1 = Terms.objects.filter()
    return render(request, 'home/terms.html', {'file':file1[len(file1)-1].file1})


def privacy(request):
    file1 = Terms.objects.filter()
    return render(request, 'home/terms.html', {'file': file1[len(file1) - 1].file2})

def ban(request):
    file1 = Terms.objects.filter()
    return render(request, 'home/terms.html', {'file': file1[len(file1) - 1].file3})

