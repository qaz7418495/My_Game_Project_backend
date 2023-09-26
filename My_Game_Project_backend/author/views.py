#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("欢迎")


def get_user_list(request):
    return HttpResponse("用户列表")


def add_user(request):
    return HttpResponse("添加用户")