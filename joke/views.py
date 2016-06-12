#coding=utf8
from django.shortcuts import render
from django.db import connection
from django.http import Http404
from django.http import HttpResponse
from utils import parse_joke
import json
from user_info.utils.parse_user import checkout_login
from models import joke_operating
from django.views.decorators.http import require_POST
import settings
from datetime import datetime

@checkout_login
def joke_index(request):
    page=request.GET.get('page',0)
    try:
        page=int(page)
    except:
        page=0
    if page<=0:
        previous_page=0
    else:
        previous_page=page-1
    cur=None
    try:
        cur=connection.cursor()
        sql="""SELECT * FROM joke LIMIT  %s,%s"""\
            %(page*10,10)
        cur.execute(sql)
        joke_dict=map(lambda x:parse_joke.process_joke__from_database(x),cur.fetchall())
        return render(request,'joke_index.html',context={'joke_list':joke_dict,'previous_page':previous_page,
                                                         'next_page':page+1})
    except Exception:
        return Http404
    finally:
        if cur:
            cur.close()

@require_POST
@checkout_login
def operating_joke_from_user(request):
    # print request.POST
    # commit_joke_data={'user_id':user_id,
    #     'joke_id':joke_id,
    #     'commit_type':commit_type,
    #     'commit_text':commit_text
    # }
    try:
        user_id=request.POST['user_id']
        joke_id=request.POST['joke_id']
        commit_type_china=request.POST['commit_type']
        commit_type=settings.JOKE_COMMIT_TYPE[commit_type_china]
        commit_text=request.POST['commit_text']
        joke_operating(joke_id_id=joke_id,operating_joke_user_id_id=user_id,
                       operating_type=commit_type,
                       operating_type_china=commit_type_china,
                       operating_text=commit_text,
                       create_time=datetime.now(),
                       update_time=datetime.now()).save()
        response_data={'state':1,'msg':u'%s'%commit_type_china}
    except KeyError as e:
        response_data={'state':0,'msg':u'%s %s'%(u'POST数据丢失键值',e)}
    except Exception as e:
        response_data={'state':0,'msg':u'%s'%e}
    response=HttpResponse(json.dumps(response_data))
    return response


