#coding=utf8
from django.shortcuts import render
from django.http import Http404,HttpResponse
from django.db import connection
import json
from django.views.decorators.http import require_POST
from utils.parse_user import checkout_login
def user_register(request):
    return render(request,'user_register.html')

@require_POST
def user_login(request):
    user_name=request.POST.get('user_name')
    user_password=request.POST.get('user_password')
    if not user_name or not user_password:
        return Http404
    cur=None
    try:
        cur=connection.cursor()
        sql="""SELECT id FROM user_info WHERE user_name='%s' and user_password='%s'"""
        cur.execute(sql%(user_name,user_password))
        user_id=cur.fetchone()
        if user_id:
            user_id=user_id[0]
            user_name=request.session.setdefault('user_name',user_name)
            content={'msg':u'登录成功','state':1}
        else:
            user_id=0
            content={'msg':u'账号或者密码错误','state':2}
    except:
        user_id=0
        content={'msg':u'登录错误','state':0}
    finally:
        if cur:
            cur.close()
    response=HttpResponse(json.dumps(content))
    response.set_cookie('user_name',value=user_name)
    response.set_cookie("user_id",value=user_id)
    return response

@require_POST
def user_out_login(request):
    try:
        del request.session["user_name"]
        out_login_content={"msg":u'注销成功','state':1}
    except:
        out_login_content={"msg":u'已经处于离线状态','state':0}
    response=HttpResponse(json.dumps(out_login_content))
    return response

@require_POST
@checkout_login
def get_user_data(request):
    user_name=request.session.get("user_name")
    cur=None
    try:
        cur=connection.cursor()
        sql="""SELECT id FROM user_info WHERE user_name='%s' """%user_name
        cur.execute(sql)
        content={'msg':user_name,'state':1}
    except:
        content={'msg':u'你没有注册','state':0}
    finally:
        if cur:
            cur.close()
    return HttpResponse(json.dumps(content))



def user_index(request):
    pass

