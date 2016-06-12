#coding=utf8

def process_joke__from_database(joke):
    """
    将 joke_list 转成 字典 joke_dict
    :param joke:
    :return: joke_dict
    """
    joke_id,state,create_time,update_time,\
    title,content,img_uuid,create_joke_user_id=joke
    joke_dict={
        'joke_id':joke_id,
        'create_time':create_time,
        'title':title,
        'content':content,
        'create_joke_user_id':create_joke_user_id,
    }
    return joke_dict