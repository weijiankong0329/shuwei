$(function() {
    var arr = ["星期日","星期一","星期二","星期三","星期四","星期五","星期六"];

    var time_show = $('#time-show');
    fn();
    var content_height = $("body").height()-$("header").height()-$("footer").height();
    $("#content-wrap").css("min-height",content_height);
    $(".admin-main-content").css("min-height",content_height);
    if($("#id_参考问答").prop('checked')){
        $("#参考问答项目-div").removeAttr("hidden");
        $("#答案-div").attr("hidden","true");
    }else{
        $("#答案-div").removeAttr("hidden");
        $("#参考问答项目-div").attr("hidden","true");
    }

    if(content_title){
        $(content_title).addClass("bg-dark text-white");
        $(task).addClass("bg-grey text-white");
        $(content_title).next('ul').attr('hidden',false);
        $(content_title).css('pointer-events','none');
        $(task).css('pointer-events','none');
    }

    function fn(response){
        var date = new Date();
        var test_Date = new Date(date).toLocaleString('en-US', {timeZone: 'Asia/Shanghai',});
        var timeArr = dateFormat(test_Date);
        console.log(test_Date);
        $(time_show).html(timeArr);
    }

    function dateFormat(d){
        var date = new Date(d);
        var YY = date.getFullYear();
        var MM = date.getMonth() + 1 ;
        var Day = date.getDay();
        var DD = date.getDate();
        var hh = addZero(date.getHours());
        var mm = addZero(date.getMinutes());
        var ss = addZero(date.getSeconds());
        return  YY + "年" + MM + "月" + DD + "日 " + arr[Day] + "<br />" + hh + "时" + mm + "分" + ss + "秒"
    }

    function addZero ( n ){
        return n < 10 ? "0" + n : n + "";
    }



   $(".admin-nav-link").click(function(){
        $(".navbar-nav-sub").attr('hidden',true);
        $(".admin-nav-link").removeClass("bg-dark text-white");
        $(".nav-link-sub").removeClass("bg-grey text-white");
        $(".admin-nav-link").css('pointer-events','');
        $(this).next('ul').children('li').first().children('a').addClass("bg-grey text-white")
        $(this).next('ul').attr('hidden',false);
        $(this).addClass("bg-dark text-white");
        $(this).css('pointer-events','none');
   });

   $(".nav-link-sub").click(function(){
        $(this).addClass("bg-grey text-white");
        $(".nav-link-sub").removeClass("bg-grey text-white");
        $(".nav-link-sub").css('pointer-events','');
        $(this).css('pointer-events','none');
   });


    $("#id_图片").change(function () {
        console.log(this);
        $("#img-preview-div").removeAttr('hidden');
        const file = this.files[0];
        if (file) {
            let reader = new FileReader();
            reader.onload = function (event) {
                $("#img-preview").attr("src", event.target.result);
            };
            reader.readAsDataURL(file);
        }
    });

    $(".comment-edit").click(function(){
        var delete_element = "#delete-"+ this.value;
        $(delete_element).removeAttr('hidden');
        $(delete_element).prev().attr('hidden','true');
        $(this).next().removeAttr('hidden');
        var comment_action_div = "#"+ this.value;
        $(comment_action_div).removeAttr('hidden');
        $(this).attr('hidden','true');
    });

     $(".comment-close").click(function(){
         $(this).prev().removeAttr('hidden');
         var delete_element = "#delete-"+ this.value;
        var comment_action_div = "#"+ this.value;
        $(comment_action_div).attr('hidden','true');
        $(this).attr('hidden','true');
        $(delete_element).attr('hidden','true');
        $(delete_element).prev().removeAttr('hidden');
    });

    $("#id_视频文件").change(function (event) {
        $("#video-preview-div").removeAttr('hidden');
        let file = event.target.files[0];
        let blobURL = URL.createObjectURL(file);
        $("#video-preview").attr("src", blobURL);
    });

    $("#id_参考问答").click(function(){
        if(this.checked){
            $("#参考问答项目-div").removeAttr("hidden");
            $("#答案-div").attr("hidden","true");

        }else{
            $("#答案-div").removeAttr("hidden");
            $("#参考问答项目-div").attr("hidden","true");
            $("#id_参考问答项目").val('');
        }
    });

    $('.add-question-btn').click(function(){
        $(this).attr('hidden','true');
        $('.add-question-section').attr('hidden','');
    });

});