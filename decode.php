<?php

$str = '39.3x5\xa7b3\xa8\x99,0\x9ep\xa3a2\xa5\xad';
echo $str;
$k = mb_convert_encoding($str, 'ascii', 'utf8');
echo PHP_EOL;
echo utf8_encode($str);
echo PHP_EOL;
echo utf8_decode($str);
