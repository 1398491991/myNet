#coding=utf8
from django.shortcuts import render

def checkout_login(func):
    def wrapper(*args, **kw):
        if args[0].session.has_key("user_name"):
            return func(*args, **kw)
        return render(args[0],'not_login.html')
    return wrapper
