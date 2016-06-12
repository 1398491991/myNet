/**
 * Created by LShu on 2016/6/8.
 */
        //<input type="text" class="form-control">
        //       <span class="input-group-btn">
        //          <button class="btn btn-default" type="button">
        //             Go!
        //          </button>
        //       </span>
        //</div>

function joke_zan(joke_id){
commit_joke_data_api(joke_id,'赞',null);
}

function joke_cai(joke_id){
    commit_joke_data_api(joke_id,'踩',null);
}

function joke_pinglun(joke_id){
    var pinglun_text=$('#'+joke_id).val();
    if(pinglun_text.length<=5){
        alert("评论字数至少5个字");
        return false
    }
    commit_joke_data_api(joke_id,'评论',pinglun_text);


}




function commit_joke_data_api(joke_id,commit_type,commit_text){
    /*
    用于提交数据  赞 踩 评论  如果 commit_type=='pinglun'
    则 commit_text 不为空 否则 为空
     */
    var user_id=$.cookie("user_id");
    if(user_id==null || user_id==""){
        alert('丢失 user_id 信息，无法评论');
        return false
    }
    commit_joke_data={'user_id':user_id,
        'joke_id':joke_id,
        'commit_type':commit_type,
        'commit_text':commit_text
    };
    $.ajax({
                //提交数据的类型 POST GET
                type:"POST",
                //提交的网址
                url:"/joke/operating_joke_from_user/",
                //提交的数据
                data:commit_joke_data,
                //返回数据的格式
                datatype: "json",//"xml", "html", "script", "json", "jsonp", "text".
                //在请求之前调用的函数
                //beforeSend:function(){$("#login_button").hide();},//把按钮影藏
                //成功返回之后调用的函数
                success:function(data){
                    data=JSON.parse(data);
                    if(data.state==1){
                        alert(data.msg+'成功')
                    }
                    else{
                        alert('操作失败 Error: '+data.msg)
                    }
                }
   ,
                //调用执行后调用的函数
                //complete: function(XMLHttpRequest, textStatus){
                //   alert(XMLHttpRequest.responseText);
                //   alert(textStatus);
                //    //HideLoading();
                //},
                //调用出错执行的函数
                error: function(msg){
                    //请求出错处理
                    //$("#login_button").show();
                    alert(msg);

                }
             });
}
//
//$('#233').on("click",function(){
//
//
//});


//$('.btn-group-sm').delegate("button","click",function(){
//    var joke_id= $(this).parent().parent().attr('id');
//    alert(joke_id);
//});