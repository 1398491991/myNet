/**
 * Created by LShu on 2016/6/7.
 */
function user_login(){
    var login_form=$("#login_form")[0];
    var user_name= login_form.elements["user_name"].value;
    var user_password =login_form.elements["user_password"].value;
    if(user_name==null || user_name==""){
        alert("账号不能为空");
        return false
    }
    if(user_password==null || user_password==""){
        alert("密码不能为空");
        return false
    }
    $.ajax({
                //提交数据的类型 POST GET
                type:"POST",
                //提交的网址
                url:"/user_info/login/",
                //提交的数据
                data:{"user_name":user_name,"user_password":user_password},
                //返回数据的格式
                datatype: "json",//"xml", "html", "script", "json", "jsonp", "text".
                //在请求之前调用的函数
                //beforeSend:function(){$("#login_button").hide();},//把按钮影藏
                //成功返回之后调用的函数
                success:function(data){
                    //$("#login_button").show();
                    data=JSON.parse(data);
                    if(data.state!=1) {
                        alert(data.msg);
                        return false
                    }
                    location.reload(true);

               //$("#msg").html(decodeURI(data));
                }  ,
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
                    alert(msg)
                }
             });
}



function user_out_login(){
    user_name=$.cookie("user_name");
    if(user_name==null){
        alert("数据丢失错误");
        return false;
    }
    $.ajax({
                //提交数据的类型 POST GET
                type:"POST",
                //提交的网址
                url:"/user_info/out_login/",
                //提交的数据
                data:{"user_name":user_name},
                //返回数据的格式
                datatype: "json",//"xml", "html", "script", "json", "jsonp", "text".
                //在请求之前调用的函数
                //beforeSend:function(){$("#login_button").hide();},//把按钮影藏
                //成功返回之后调用的函数
                success:function(data){
                    //$("#login_button").show();
                    data=JSON.parse(data);
                    alert(data.msg);
                    if(data.state!=1){
                        return false
                    }
                    location.reload(true);

               //$("#msg").html(decodeURI(data));
                }  ,
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



function get_user_data(){
    user_name=$.cookie("user_name");
    if(user_name==null){
        $('#user_info').children().eq(0).remove();
        return false
    }
    $.ajax({
                //提交数据的类型 POST GET
                type:"POST",
                //提交的网址
                url:"/user_info/get_user_data/",
                //提交的数据
                data:{"user_name":user_name},
                //返回数据的格式
                datatype: "json",//"xml", "html", "script", "json", "jsonp", "text".
                //在请求之前调用的函数
                //beforeSend:function(){$("#login_button").hide();},//把按钮影藏
                //成功返回之后调用的函数
                success:function(data){
                    //$("#login_button").show();
                    try {
                        data=JSON.parse(data);
                    if(data.state==1){

                        $('#user_info').children().eq(1).remove();
                        $('#user_register').remove();
                    }
                    else {
                            alert(data.msg);
                            location.href="/user_info/register/";
                        }
                    }catch(e){
                        $('#user_info').children().eq(0).remove();
                    }

               //$("#msg").html(decodeURI(data));
                }  ,
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





$(document).ready(function(){
//get_user_data();


});