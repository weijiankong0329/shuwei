$(function() {
    var arr = ["星期日","星期一","星期二","星期三","星期四","星期五","星期六"];

    var time_show = $('#time-show');
    fn();

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
});