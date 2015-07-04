<?php

$url = "http://172.20.1.61/web200/";
$data = array(
    "give_me_flag" => "1",
);
$data = http_build_query($data, "", "&");

//header
$header = array(
    "Content-Type: application/x-www-form-urlencoded",
    "Content-Length: ".strlen($data)
);

$context = array(
    "http" => array(
    "method"  => "POST",
    "header"  => implode("\r\n", $header),
    "content" => $data
)
);
$f = file_get_contents($url, false, stream_context_create($context));

var_dump($f);
