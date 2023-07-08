var now = moment();
var timeInShanghai = now.tz('Asia/Shanghai').format('h:mma');
document.getElementById('date-time').innerHTML=timeInShanghai;