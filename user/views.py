from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login,logout
from manage import main
from .models import User
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import HttpResponse
from django.views.generic import RedirectView
from rest_framework.response import Response
from rest_framework import generics
import json
from django.contrib import messages
from django.template import RequestContext
from django.views.generic import ListView
from django.utils.decorators import method_decorator
# Create your views here.
from rest_framework import viewsets

@csrf_exempt
def join(request):
    print(request)
    id = request.POST['user_id']
    name = request.POST['user_name']
    email = request.POST['email_addr']
    pw = request.POST['user_pw']
    pw2 = request.POST['user_pw2']

    user = User(user_id=id, user_name=name, email_addr=email, user_pw=pw, user_pw2=pw2)
    user.set_password(pw)
    user.save()
    print(request)
    return render(request,'login.html')

@csrf_exempt
def idconfirm(request):
    print(request)
    user_id = request.POST['inputId']

    try :
        compare_id = str(User.object.get(user_id=user_id))
    except:
        compare_id = '';

    if user_id == compare_id:
        context = {'canUse': False }
        return HttpResponse(json.dumps(context), content_type='application/json')
    else:
        context = {'canUse': True }
        return HttpResponse(json.dumps(context), content_type='application/json')

@csrf_exempt
def emailconfirm(request):
    email_addr = request.POST['email_addr']
    print(email_addr)
    data ='';
    try :
        compare_data = User.object.get(email_addr=email_addr)
        data = compare_data.email_addr
    except:
        compare_data = '';
    print("compare_email = ",data)
    if email_addr in data:
        context = {'canUse': False }
        return HttpResponse(json.dumps(context), content_type='application/json')
    else:
        context = {'canUse': True }
        return HttpResponse(json.dumps(context), content_type='application/json')


@csrf_exempt
def log_in(request):
    user_id = request.POST['inputId']
    user_pw = request.POST['inputPassword']
    try:
        user_active = User.object.get(user_id=user_id)
    except Exception:
        msg = '아이디, 비밀번호를 확인해주세요.'
        return render(request, 'msg/errorPage.html', {'msg': msg})

    if user_active.is_active:
        user = authenticate(request, username=user_id, password=user_pw)
        print(user_id)
        print(user_pw)
        print('user=', user)
        if user is not None:
            login(request, user)
            request.session['user_id'] = request.POST['inputId']
            return redirect('/page/main')
        else:
            msg = '아이디, 비밀번호를 확인해주세요.'
            return render(request, 'msg/errorPage.html', {'msg': msg})

def log_out(request):
    logout(request)
    return redirect('/')