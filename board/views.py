from django.shortcuts import render, redirect, get_object_or_404
from .models import Board,Photo,User
from django.http import HttpResponse
import json
# Create your views here.

# def getData(request):
#     board = Board.objects.all()
#     print(board)
#     return render(request,'main.html',{'board': board})


def board_Detail(request, pk):
    detail_data = Board.objects.get(id=pk)
    photo_data = Photo.objects.all().filter(board_id=pk)
    isWriter = ''
    if str(detail_data.writer) == str(request.session['user_id']):
        isWriter = True
    return render(request, 'detail.html', {'detail_data':detail_data, 'photo_data':photo_data, 'isWriter':isWriter})


def board_create(request):
    if request.method == 'POST':
        board = Board()
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.category = 'test'
        board.writer = User.object.get(user_id=request.session['user_id'])
        board.save()
        print("userid= ", board.writer)
        for img in request.FILES.getlist('imgs'):
            photo = Photo()
            photo.board = board
            photo.image = img
            photo.save()
        return redirect('/page/main/')

def board_Edit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.save()
        photo = Photo.objects.filter(board_id=pk)
        photo.delete()
        for img in request.FILES.getlist('imgs'):
            photo_upd = Photo()
            photo_upd.board = board
            photo_upd.image = img
            photo_upd.save()
        return redirect('/page/main/')
    else:
        msg = '전송 오류'
        return render(request, 'msg/errorPage.html', {'msg':msg})

def board_delete(request,pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('/page/main/')

def like(request, pk):
    board = Board.objects.get(id=pk)
    # if request.user.id in board.writer.pk:
    if request.user in board.like_users.all():
        board.like_users.remove(request.user.id)
        board.boardLike -= 1
        board.save()
    else:
        board.like_users.add(request.user.id)
        board.boardLike += 1
        board.save()

    return redirect('/board/board_detail/'+str(pk))