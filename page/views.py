from django.shortcuts import render, redirect
from board.models import Board,Photo
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

# Create your views here.


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

def go_main(request):
    board = Board.objects.all().order_by('id')
    page = request.GET.get('page')
    paginator = Paginator(board, 20)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)

    leftIndex = (int(page) - 5)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex+1)

    return render(request,'main.html',{'board': board, 'page_obj':page_obj, 'paginator':paginator, 'custom_range':custom_range})
    # return render(request, 'main.html')

def board_reg(request):
    return render(request, 'board_reg.html')

def board_update(request, pk):
    board = Board.objects.get(id=pk)
    return render(request, 'board_reg.html',{'board':board})