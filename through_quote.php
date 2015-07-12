<?php


# 前後のチェック漏れ
$v = "00-00-0000'";
var_dump(!!preg_match("/[0-9]{2,4}-[0-9]{2,4}-[0-9]{4}/", $v));

# 改行文字抜け (ereg Deprecated PHP >= 6.0)
$v = "00-00-0000\00'";
# "00-00-0000%00'";
var_dump(!!@ereg("^[0-9]{2,4}-[0-9]{2,4}-[0-9]{4}$", $v));


$v = "00-00-0000\n'";
# "00-00-0000%0a'";
var_dump((preg_match("/(.*)-(.*)-(.*)/", $v, $match)) &&
    (!empty($match[1]) && !empty($match[2]) && !empty($match[3])) &&
    (is_numeric(trim($match[1].$match[2].$match[3])))
);

# pcre background_limit
$v = "'" . str_repeat("_", 10000001);
var_dump(!preg_match("/.*'.*/s", $v));
